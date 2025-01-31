from holos_service.common import verify_is_prairie_province
from holos_service.components.land_management.common import TillageType
from holos_service.config import PathsHolosResources
from holos_service.django_stuff import CanadianProvince
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


def calculate_tillage_factor_for_perennials(
        soil_functional_category: SoilFunctionalCategory,
        province: CanadianProvince
) -> float:
    """Returns the value of the tillage factor for perennial crops.

    Args:
        soil_functional_category: SoilFunctionalCategory class member
        province: CanadianProvince class member

    Returns:
        (-) value of the tillage factor for perennial crops

    Holos source code:
        https://github.com/holos-aafc/Holos/blob/90fad0a9950183da217137490cb756104ba3f7f4/H.Core/Calculators/Tillage/TillageFactorCalculator.cs#L138
    """
    if not verify_is_prairie_province(province=province):
        res = 0.9
    else:
        res = calculate_crop_tillage_factor(
            soil_functional_category=soil_functional_category,
            tillage_type=TillageType.NoTill)
    return res
