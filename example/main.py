from datetime import datetime, timedelta
from pathlib import Path

from pandas import read_csv

from example.beef_inputs import set_beef_data
from example.dairy_inputs import set_dairy_data
from example.sheep_inputs import set_sheep_data
from holos_service.farm.farm import create_farm
from holos_service.farm.farm_inputs import WeatherSummary


def set_weather_summary() -> WeatherSummary:
    df = read_csv('weather_data.csv', sep=',', decimal='.', comment='#')
    year = df.loc[0, 'year']
    date_base = datetime(year - 1, 12, 31)
    df['date'] = df['day_of_year'].apply(lambda x: date_base + timedelta(x))
    gdf = df.groupby(df['date'].dt.month)
    precipitation = gdf['precipitation'].sum()
    etp = gdf['potential_evapotranspiration'].sum()
    return WeatherSummary(
        year=2024,
        mean_annual_precipitation=542,
        mean_annual_temperature=3.57,
        mean_annual_evapotranspiration=626,
        growing_season_precipitation=precipitation[(precipitation.index > 4) & (precipitation.index < 12)].sum(),
        growing_season_evapotranspiration=etp[(etp.index > 4) & (etp.index < 12)].sum(),
        monthly_precipitation=precipitation.tolist(),
        monthly_potential_evapotranspiration=etp.tolist(),
        monthly_temperature=gdf['air_temperature'].mean().to_list())


if __name__ == '__main__':
    path_root = Path(__file__).parent
    weather_summary = set_weather_summary()
    create_farm(
        latitude=49.98,
        longitude=-98.04,
        weather_summary=set_weather_summary(),
        path_dir_farm=path_root / 'example_farm',
        beef_cattle_data=set_beef_data(weather_summary=weather_summary),
        dairy_cattle_data=set_dairy_data(weather_summary=weather_summary),
        sheep_flock_data=set_sheep_data(weather_summary=weather_summary)
    )
