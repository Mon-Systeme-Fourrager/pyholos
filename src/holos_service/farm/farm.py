from pathlib import Path

from holos_service.django_stuff import CanadianProvince
from holos_service.farm.farm_inputs import BeefCattleInput, DairyCattleInput, SheepFlockInput, FarmGeneralInfo
from holos_service.soil import SoilTexture


def write_animal_input_csv(
        animal_data: BeefCattleInput | DairyCattleInput | SheepFlockInput,
        province: CanadianProvince,
        soil_texture: SoilTexture,
        path_dir_animal: Path,
) -> None:
    dfs = animal_data.create_components(
        province=province,
        soil_texture=soil_texture)
    for df in dfs:
        name_output_file = df['Name'].unique()[0]

        df.to_csv(path_dir_animal / f'{name_output_file}.csv', index=False)

    pass


def create_farm(
        farm_general_info: FarmGeneralInfo,
        path_dir_farm: Path,
        beef_cattle_data: BeefCattleInput = None,
        dairy_cattle_data: DairyCattleInput = None,
        sheep_flock_data: SheepFlockInput = None,
        field_data=None,
) -> None:
    path_dir_farm.mkdir(parents=True, exist_ok=True)
    farm_general_info.set_farm_settings().write(path_dir_farm=path_dir_farm)

    for animal_data, dir_name in [
        (beef_cattle_data, 'Beef'),
        (dairy_cattle_data, 'Dairy'),
        (sheep_flock_data, 'Sheep')]:
        if animal_data is not None:
            path_dir_animal = path_dir_farm / dir_name
            path_dir_animal.mkdir(parents=True, exist_ok=True)

            write_animal_input_csv(
                animal_data=animal_data,
                province=farm_general_info.province,
                soil_texture=farm_general_info.soil_texture,
                path_dir_animal=path_dir_farm / dir_name
            )

    pass
