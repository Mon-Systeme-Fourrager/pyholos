import math


def calculate_green_area_index_max(
        crop_yield: float
) -> float:
    """Calculates the maximum amplitude of green area index

    Args:
        crop_yield: (kg(DM)/ha) crop yield

    Returns:
        (m2(green area)/m2(ground)) maximum amplitude of green area index

    Holos source code:
        https://github.com/holos-aafc/Holos/blob/8a3d8fb047c2058a3dbe273f5a8550ae63a54f14/H.Core/Calculators/Climate/ClimateParameterCalculator.cs#L443
    """
    return 0.0731 * (crop_yield / 1000) ** 2 + 0.408 * crop_yield / 1000


def calculate_mid_season(
        emergence_day: int,
        ripening_day: int
) -> int | float:
    """Calculates the maximum amplitude of green area index

    Args:
        emergence_day: (Julian day) day of crop emergence
        ripening_day: (Julian day) day of crop ripening

    Returns:
        (Julian day) median day of the growing season

    Holos source code:
        https://github.com/holos-aafc/Holos/blob/8a3d8fb047c2058a3dbe273f5a8550ae63a54f14/H.Core/Calculators/Climate/ClimateParameterCalculator.cs#L453
    """
    return emergence_day + (ripening_day - emergence_day) / 2


def calculate_green_area_index(
        green_area_index_max: float,
        julian_day: int,
        mid_season: float,
        variance: float
) -> float:
    """Calculates the green area index at a given day

    Args:
        green_area_index_max: (m2(green area)/m2(ground)) maximum amplitude of green area index
        julian_day: (julian day) day
        mid_season: (Julian day) median day of the growing season
        variance: width of distribution function

    Returns:
        (m2(green area)/m2(ground)) green area index

    Holos source code:
        https://github.com/holos-aafc/Holos/blob/8a3d8fb047c2058a3dbe273f5a8550ae63a54f14/H.Core/Calculators/Climate/ClimateParameterCalculator.cs#L463
    """
    return green_area_index_max * math.exp((-1 * (julian_day - mid_season) ** 2) / (2 * variance))


def calculate_organic_carbon_factor(
        percent_organic_carbon: float
) -> float:
    """Calculates the organic carbon factor (OrgC_factor)

    Args:
        percent_organic_carbon: (%) percentage of organic C in soil, by weight

    Returns:
        (-) organic carbon factor (OrgC_factor)

    Holos source code:
        https://github.com/holos-aafc/Holos/blob/8a3d8fb047c2058a3dbe273f5a8550ae63a54f14/H.Core/Calculators/Climate/ClimateParameterCalculator.cs#L474
    """
    return -0.837531 + 0.430183 * percent_organic_carbon


def calculate_clay_factor(
        clay_content: float
) -> float:
    """Calculates the clay factor

    Args:
        clay_content: proportion of clay in soil (Clay_factor)

    Returns:
        (-) clay factor

    Holos source code:
        https://github.com/holos-aafc/Holos/blob/8a3d8fb047c2058a3dbe273f5a8550ae63a54f14/H.Core/Calculators/Climate/ClimateParameterCalculator.cs#L484
    """
    return -1.40744 + 0.0661969 * clay_content * 100
