from enum import Enum
from os import environ
from pathlib import Path

PATH_HOLOS_CLI = Path(environ['PATH_HOLOS_CLI'])


class PathsSlcData(Enum):
    path_root = Path(environ['PATH_SLC_DATA'])
    geojson_file = path_root / 'soil_landscapes_of_canada_v3r2.geojson'
    csv_dir = path_root / 'soil_landscapes_of_canada_v3r2_csv'
    cmp_file = csv_dir / 'ca_all_slc_v3r2_cmp.csv'
    slt_file = csv_dir / 'ca_all_slc_v3r2_slt.csv'
    snt_file = csv_dir / 'ca_all_slc_v3r2_snt.csv'
