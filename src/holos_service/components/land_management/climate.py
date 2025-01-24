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
