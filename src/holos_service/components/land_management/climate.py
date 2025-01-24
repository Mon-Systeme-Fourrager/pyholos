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
