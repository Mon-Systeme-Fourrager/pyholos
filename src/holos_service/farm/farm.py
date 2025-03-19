from pathlib import Path

from holos_service.components.common import convert_province_name
from holos_service.django_stuff import CanadianProvince
from holos_service.farm.farm_inputs import (BeefCattleInput, DairyCattleInput, SheepFlockInput, WeatherSummary)
from holos_service.farm.farm_settings import ParamsFarmSettings
from holos_service.soil import (SoilTexture, convert_soil_texture_name, convert_soil_functional_category_name,
                                SoilFunctionalCategory)


def write_input_csv(
        dfs: list[DataFrame],
        path_dir: Path
) -> None:
    for df in dfs:
        name_output_file = df['Name'].unique()[0]
        df.to_csv(path_dir / f'{name_output_file}.csv', index=False)
    pass


def write_animal_input_csv(
        animal_data: BeefCattleInput | DairyCattleInput | SheepFlockInput,
        province: CanadianProvince,
        soil_texture: SoilTexture,
        path_dir_animal: Path,
) -> None:
    write_input_csv(
        dfs=animal_data.create_components(
            province=province,
            soil_texture=soil_texture),
        path_dir=path_dir_animal
    )

        df.to_csv(path_dir_animal / f'{name_output_file}.csv', index=False)

    pass


def create_farm(
        latitude: float,
        longitude: float,
        weather_summary: WeatherSummary,
        path_dir_farm: Path,
        beef_cattle_data: BeefCattleInput = None,
        dairy_cattle_data: DairyCattleInput = None,
        sheep_flock_data: SheepFlockInput = None,
        field_data=None,
) -> None:
    path_dir_farm.mkdir(parents=True, exist_ok=True)
    farm_settings = ParamsFarmSettings(
        latitude=latitude,
        longitude=longitude,
        year=weather_summary.year,
        monthly_precipitation=weather_summary.monthly_precipitation,
        monthly_potential_evapotranspiration=weather_summary.monthly_potential_evapotranspiration,
        monthly_temperature=weather_summary.monthly_temperature)

    farm_settings.write(path_dir_farm=path_dir_farm)

    params_soil = farm_settings.params_soil

    province = convert_province_name(name=params_soil.province.value)
    soil_texture = convert_soil_texture_name(name=params_soil.soil_texture.value)

    for animal_data, dir_name in [
        (beef_cattle_data, 'Beef'),
        (dairy_cattle_data, 'Dairy'),
        (sheep_flock_data, 'Sheep')]:
        if animal_data is not None:
            path_dir_animal = path_dir_farm / dir_name
            path_dir_animal.mkdir(parents=True, exist_ok=True)

            write_animal_input_csv(
                animal_data=animal_data,
                province=province,
                soil_texture=soil_texture,
                path_dir_animal=path_dir_farm / dir_name
            )

    pass
