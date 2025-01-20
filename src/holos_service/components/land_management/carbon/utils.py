from holos_service.components.common import convert_province_name
from holos_service.components.land_management.crop import convert_crop_type_name, CropType
from holos_service.config import PathsHolosResources
from holos_service.utils import read_holos_resource_table


class LoadedData:
    def __init__(self):
        self.table_small_yield_area = self.read_small_yield_area_data()

    @staticmethod
    def read_small_yield_area_data():
        """Loads default yield data table.

        Holos source code:
            https://github.com/holos-aafc/Holos/blob/d6dba2d07413fd2d23439b60a6bb9217c8ebb048/H.Core/Providers/Soil/SmallAreaYieldProvider.cs#L113
        """
        excluded_cols = [4, 14, 15, 19, 20, 37, 38, 40]
        df = read_holos_resource_table(
            path_file=PathsHolosResources.Table_small_area_yields,
            usecols=[v for v in range(41) if v not in excluded_cols])

        columns = list(df.columns[:4]) + [convert_crop_type_name(name=v).value for v in df.columns[4:]]

        for crop, replacing_crop in [
            (CropType.MustardSeed, CropType.Mustard),
            (CropType.DryFieldPeas, CropType.DryPeas),
            (CropType.TimothyHay, CropType.TamePasture)
        ]:
            columns[columns.index(crop)] = replacing_crop

        df.columns = columns
        df['PROVINCE'] = df['PROVINCE'].apply(lambda x: convert_province_name(name=x).name)
        return df
