from holos_service.components.land_management.common import TillageType
from holos_service.config import PathsHolosResources
from holos_service.soil import SoilFunctionalCategory
from holos_service.utils import read_holos_resource_table

TABLE_TILLAGE_FACTOR = read_holos_resource_table(
    PathsHolosResources.Table_Tillage_Factor,
    index_col=('SoilFunctionalCategory', 'TillageType'))


def calculate_crop_tillage_factor(
        soil_functional_category: SoilFunctionalCategory,
        tillage_type: TillageType
) -> float:
    """

    Args:
        soil_functional_category: SoilFunctionalCategory class member
        tillage_type: TillageType class member

    Returns:
        (-) tillage factor

    Holos source code:
        https://github.com/holos-aafc/Holos/blob/b73623b6beec5ac2e9fea747c0ff5be0477038fa/H.Core/Calculators/Tillage/TillageFactorCalculator.cs#L153

    Note:
        "Calculates the tillage factor for various types. Table 3 -  rc factor – Alberta, Saskatchewan, Manitoba only."
    """
    try:
        res = TABLE_TILLAGE_FACTOR.loc[(soil_functional_category, tillage_type), 'TillageFactor']
    except KeyError:
        res = 1.

    return res
