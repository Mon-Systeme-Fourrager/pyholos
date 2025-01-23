from pandas import MultiIndex

from holos_service.components.common import convert_province_name
from holos_service.components.land_management.common import convert_tillage_type_name
from holos_service.components.land_management.crop import convert_crop_type_name
from holos_service.config import PathsHolosResources
from holos_service.soil import convert_soil_functional_category_name
from holos_service.utils import read_holos_resource_table


def read_table_50():
    df = read_holos_resource_table(PathsHolosResources.Table_50_Fuel_Energy_Requirement_Estimates_By_Region,
                                   header=[0, 1, 2])
    df.index = [convert_crop_type_name(s) for s in df.pop(('Unnamed: 0_level_0', 'Unnamed: 0_level_1', 'CROP'))]
    df.columns = MultiIndex.from_tuples(
        [(convert_province_name(p), convert_soil_functional_category_name(s), convert_tillage_type_name(t))
         for p, s, t in df.columns])

    return df

class HolosTables:
    Table_50_Fuel_Energy_Requirement_Estimates_By_Region = read_table_50()
