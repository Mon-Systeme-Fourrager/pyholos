from pathlib import Path

from example.farm_infos import FARM_INFO
from example.beef_inputs import set_beef_data
from example.dairy_inputs import set_dairy_data
from example.sheep_inputs import set_sheep_data
from holos_service.farm.farm import create_farm


if __name__ == '__main__':
    path_root = Path(__file__).parent
    create_farm(
        farm_general_info=FARM_INFO,
        path_dir_farm=path_root / 'example_farm',
        beef_cattle_data=set_beef_data(),
        dairy_cattle_data=set_dairy_data(),
        sheep_flock_data=set_sheep_data()
    )
