from holos_service.django_stuff import CanadianProvince
from holos_service.farm import farm_inputs
from holos_service.soil import SoilTexture

WEATHER_SUMMARY = farm_inputs.WeatherSummary(
    year=2024,
    mean_annual_precipitation=542,
    mean_annual_temperature=3.57,
    mean_annual_evapotranspiration=626,
    growing_season_precipitation=411,
    growing_season_evapotranspiration=573,
    monthly_precipitation=[16, 18, 30, 41, 121, 143, 76, 47, 38, 16, 56, 32],
    monthly_potential_evapotranspiration=[0, 0, 1, 54, 89, 122, 134, 112, 83, 37, 7, 0],
    monthly_temperature=[-13.1, -6.8, -6.4, 6.6, 12.4, 16.9, 21.9, 20.7, 18.7, 8.3, -2.7, -11.5]
)

PROVINCE = CanadianProvince.Manitoba
SOIL_TEXTURE = SoilTexture.Fine
