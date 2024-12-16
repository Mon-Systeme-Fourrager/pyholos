from enum import Enum
from os import environ
from pathlib import Path

PATH_HOLOS_CLI = Path(environ['PATH_HOLOS_CLI'])
DATE_FMT = "%Y-%m-%d"

_PATH_HOLOS_SERVICE_RESOURCES = Path(__file__).parent / 'resources'


class PathsHolosResources:
    _path_root = _PATH_HOLOS_SERVICE_RESOURCES / 'holos'
    Table_16_Livestock_Coefficients_BeefAndDairy_Cattle_Provider = _path_root / (
        'Table_16_Livestock_Coefficients_BeefAndDairy_Cattle_Provider.csv')
    Table_21_Average_Milk_Production_For_Dairy_Cows_By_Province = _path_root / (
        'Table_21_Average_Milk_Production_For_Dairy_Cows_By_Province.csv')
    Table_30_Default_Bedding_Material_Composition_Provider = _path_root / (
        'Table_30_Default_Bedding_Material_Composition_Provider.csv')


class PathsSlcData(Enum):
    _path_root = _PATH_HOLOS_SERVICE_RESOURCES / 'soil_landscapes_of_canada_v3r2'
    geojson_file = _path_root / 'soil_landscapes_of_canada_v3r2.geojson'
    csv_dir = _path_root / 'soil_landscapes_of_canada_v3r2_csv'
    cmp_file = csv_dir / 'ca_all_slc_v3r2_cmp.csv'
    slt_file = csv_dir / 'ca_all_slc_v3r2_slt.csv'
    snt_file = csv_dir / 'ca_all_slc_v3r2_snt.csv'
