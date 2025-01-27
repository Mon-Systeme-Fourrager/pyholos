import math
import sys

from holos_service.defaults import Defaults


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


def calculate_sand_factor(
        sand_content: float
) -> float:
    """Calculates the sand factor

    Args:
        sand_content: proportion of sand in soil (Sand_factor)

    Returns:
        (-) sand factor

    Holos source code:
        https://github.com/holos-aafc/Holos/blob/8a3d8fb047c2058a3dbe273f5a8550ae63a54f14/H.Core/Calculators/Climate/ClimateParameterCalculator.cs#L494
    """
    return -1.51866 + 0.0393284 * sand_content * 100


def calculate_wilting_point(
        organic_carbon_factor: float,
        clay_factor: float,
        sand_factor: float
) -> float:
    """Calculates the volumetric water content at wilting point

    Args:
        organic_carbon_factor: (-) organic carbon factor (OrgC_factor)
        clay_factor: (-) clay factor
        sand_factor: (-) sand factor

    Returns:
        (mm3/mm3) volumetric water content at wilting point

    Holos source code:
        https://github.com/holos-aafc/Holos/blob/8a3d8fb047c2058a3dbe273f5a8550ae63a54f14/H.Core/Calculators/Climate/ClimateParameterCalculator.cs#L504
    """
    wilting_point_percent = 14.2568 + 7.36318 * (
            0.06865 + 0.108713 * organic_carbon_factor -
            0.0157225 * organic_carbon_factor ** 2 +
            0.00102805 * organic_carbon_factor ** 3 +
            0.886569 * clay_factor -
            0.223581 * organic_carbon_factor * clay_factor +
            0.0126379 * organic_carbon_factor ** 2 * clay_factor -
            0.017059 * clay_factor ** 2 +
            0.0135266 * organic_carbon_factor * clay_factor ** 2 -
            0.0334434 * clay_factor ** 3 -
            0.0535182 * sand_factor -
            0.0354271 * organic_carbon_factor * sand_factor -
            0.00261313 * organic_carbon_factor ** 2 * sand_factor -
            0.154563 * clay_factor * sand_factor -
            0.0160219 * organic_carbon_factor * clay_factor * sand_factor -
            0.0400606 * clay_factor ** 2 * sand_factor -
            0.104875 * sand_factor ** 2 +
            0.0159857 * organic_carbon_factor * sand_factor ** 2 -
            0.0671656 * clay_factor * sand_factor ** 2 -
            0.0260699 * sand_factor ** 3)

    return wilting_point_percent / 100.


def calculate_field_capacity(
        organic_carbon_factor: float,
        clay_factor: float,
        sand_factor: float
) -> float:
    """Calculates the volumetric water content at field capacity

    Args:
        organic_carbon_factor: (-) organic carbon factor (OrgC_factor)
        clay_factor: (-) clay factor
        sand_factor: (-) sand factor

    Returns:
        (mm3/mm3) volumetric water content at field capacity

    Holos source code:
        https://github.com/holos-aafc/Holos/blob/8a3d8fb047c2058a3dbe273f5a8550ae63a54f14/H.Core/Calculators/Climate/ClimateParameterCalculator.cs#L543
    """
    field_capacity_percent = 29.7528 + 10.3544 * (
            0.0461615 + 0.290955 * organic_carbon_factor -
            0.0496845 * organic_carbon_factor * organic_carbon_factor +
            0.00704802 * organic_carbon_factor * organic_carbon_factor * organic_carbon_factor +
            0.269101 * clay_factor -
            0.176528 * organic_carbon_factor * clay_factor +
            0.0543138 * organic_carbon_factor * organic_carbon_factor * clay_factor +
            0.1982 * clay_factor * clay_factor -
            0.060699 * clay_factor * clay_factor * clay_factor -
            0.320249 * sand_factor -
            0.0111693 * organic_carbon_factor * organic_carbon_factor * sand_factor +
            0.14104 * clay_factor * sand_factor +
            0.0657345 * organic_carbon_factor * clay_factor * sand_factor -
            0.102026 * clay_factor * clay_factor * sand_factor -
            0.04012 * sand_factor * sand_factor +
            0.160838 * organic_carbon_factor * sand_factor * sand_factor -
            0.121392 * clay_factor * sand_factor * sand_factor -
            0.061667 * sand_factor * sand_factor * sand_factor)

    return field_capacity_percent / 100.


def calculate_soil_mean_depth() -> float:
    """Calculates the soil top layer mean depth

    Returns:
        (mm) soil top layer mean depth

    Holos source code:
        https://github.com/holos-aafc/Holos/blob/8a3d8fb047c2058a3dbe273f5a8550ae63a54f14/H.Core/Calculators/Climate/ClimateParameterCalculator.cs#L581

    Note:
        Holos assumes the value of layer_thickness constant to 250 mm
    """
    return Defaults.TopLayerThickness / 20.


def calculate_leaf_area_index(
        green_area_index: float
) -> float:
    """Calculates the leaf area index

    Args:
        green_area_index: (m2(green area)/m2(ground)) green area index

    Returns:
        (m2(leaf)/m2(ground)) leaf area index

    Holos source code:
        https://github.com/holos-aafc/Holos/blob/8a3d8fb047c2058a3dbe273f5a8550ae63a54f14/H.Core/Calculators/Climate/ClimateParameterCalculator.cs#L591
    """
    return 0.8 * green_area_index


def calculate_surface_temperature(
        temperature: float,
        leaf_area_index: float
) -> float:
    """Calculates the soil surface temperature

    Args:
        temperature: (degrees Celsius) daily mean air temperature by month
        leaf_area_index: (m2(leaf)/m2(ground)) leaf area index

    Returns:
        (degrees Celsius) soil surface temperature

    Holos source code:
        https://github.com/holos-aafc/Holos/blob/8a3d8fb047c2058a3dbe273f5a8550ae63a54f14/H.Core/Calculators/Climate/ClimateParameterCalculator.cs#L602
    """
    return 0.20 * temperature if temperature < 0 else (
            temperature * (0.95 + 0.05 * math.exp(-0.4 * (leaf_area_index - 3))))


def calculate_soil_temperatures(
        julian_day: int,
        soil_mean_depth: float,
        green_area_index: float,
        surface_temperature: float,
        soil_temperature_previous: float
) -> float:
    """calculates the soil temperature

    Args:
        julian_day: (julian day) day
        soil_mean_depth: (mm) soil top layer mean depth
        green_area_index: (m2(green area)/m2(ground)) green area index
        surface_temperature: (degrees Celsius) soil surface temperature
        soil_temperature_previous: (degrees Celsius) soil surface temperature of the previous day

    Returns:
        (degrees Celsius) soil temperature

    Holos source code:
        https://github.com/holos-aafc/Holos/blob/8a3d8fb047c2058a3dbe273f5a8550ae63a54f14/H.Core/Calculators/Climate/ClimateParameterCalculator.cs#L621
    """
    if julian_day == 1:
        current_soil_temperature = 0
    else:
        current_soil_temperature = soil_temperature_previous + (surface_temperature - soil_temperature_previous) * (
                0.24 * math.exp(-soil_mean_depth * 0.017) * math.exp(-0.15 * green_area_index))

    return current_soil_temperature


def calculate_crop_coefficient(
        green_area_index: float
) -> float:
    """Calculates the crop coefficient

    Args:
        green_area_index: (m2(green area)/m2(ground)) green area index

    Returns:
        (-) crop coefficient

    Holos source code:
        https://github.com/holos-aafc/Holos/blob/8a3d8fb047c2058a3dbe273f5a8550ae63a54f14/H.Core/Calculators/Climate/ClimateParameterCalculator.cs#L646
    """
    return 1.3 - (1.3 - 0.8) * math.exp(-0.17 * green_area_index)


def calculate_crop_evapotranspiration(
        evapotranspiration: float,
        crop_coefficient: float
) -> float:
    """Calculates crop evapotranspiration

    Args:
        evapotranspiration: (mm/d) reference crop evapotranspiration
        crop_coefficient: (-) crop coefficient

    Returns:
        (mm/d) crop evapotranspiration

    Holos source code:
        https://github.com/holos-aafc/Holos/blob/8a3d8fb047c2058a3dbe273f5a8550ae63a54f14/H.Core/Calculators/Climate/ClimateParameterCalculator.cs#L656
    """
    return evapotranspiration * crop_coefficient


def calculate_crop_interception(
        total_daily_precipitation: float,
        green_area_index: float,
        crop_evapotranspiration: float
) -> float:
    """Calculates crop interception

    Args:
        total_daily_precipitation: (mm/d) daily precipitation
        green_area_index: (m2(green area)/m2(ground)) green area index
        crop_evapotranspiration: (mm/d) crop evapotranspiration

    Returns:
        (mm/d) crop interception

    Holos source code:
        https://github.com/holos-aafc/Holos/blob/8a3d8fb047c2058a3dbe273f5a8550ae63a54f14/H.Core/Calculators/Climate/ClimateParameterCalculator.cs#L668
    """
    return min(crop_evapotranspiration, min(0.2 * green_area_index, total_daily_precipitation))


def calculate_soil_available_water(
        total_daily_precipitation: float,
        crop_interception: float
) -> float:
    """Calculates the available daily water for soil

    Args:
        total_daily_precipitation: (mm/d) total precipitation
        crop_interception: (mm/d) crop interception

    Returns:
        (mm) available daily water for soil

    Holos source code:
        https://github.com/RamiALBASHA/Holos/blob/06918a38b63407808e06683036639ca4afe04332/H.Core/Calculators/Climate/ClimateParameterCalculator.cs#L694
    """
    return total_daily_precipitation - crop_interception


def calculate_volumetric_soil_water_content(
        water_storage_previous: float,
        layer_thickness: float,
        wilting_point: float
) -> float:
    """Calculates the volumetric water content of soil

    Args:
        water_storage_previous: (mm day-1) soil available water of the previous day
        layer_thickness: (mm) soil layer thickness
        wilting_point: (mm3/mm3) volumetric water content at wilting point

    Returns:
        (mm3/mm3) volumetric water content

    Holos source code:
        https://github.com/holos-aafc/Holos/blob/8a3d8fb047c2058a3dbe273f5a8550ae63a54f14/H.Core/Calculators/Climate/ClimateParameterCalculator.cs#L713
    """
    volumetric_soil_water_content = water_storage_previous / layer_thickness

    if abs(volumetric_soil_water_content) < sys.float_info.epsilon:
        volumetric_soil_water_content = wilting_point

    return volumetric_soil_water_content


def calculate_soil_coefficient(
        field_capacity: float,
        volumetric_soil_water_content: float,
        wilting_point: float,
        alfa: float = 0.7
) -> float:
    """Calculates the soil coefficient of the actual crop evapotranspiration

    Args:
        field_capacity: (mm3/mm3) volumetric water content at field capacity
        volumetric_soil_water_content: (mm3/mm3) volumetric water content
        wilting_point: (mm3/mm3) volumetric water content at wilting point
        alfa: (-) minimum water storage fraction of wilting_point

    Returns:
        (-) soil coefficient for evapotranspiration

    Holos source code:
        https://github.com/holos-aafc/Holos/blob/8a3d8fb047c2058a3dbe273f5a8550ae63a54f14/H.Core/Calculators/Climate/ClimateParameterCalculator.cs#L732
    """
    soil_coefficient = min(
        1., max(0.,
                (1 - (0.95 * field_capacity - volumetric_soil_water_content) / (
                        0.95 * field_capacity - alfa * wilting_point)) ** 2))

    return 0 if (volumetric_soil_water_content < alfa / 100 * wilting_point) else soil_coefficient


def calculate_actual_evapotranspiration(
        crop_potential_evapotranspiration: float,
        soil_coefficient: float
) -> float:
    """Calculates the actual evapotranspiration of the crop

    Args:
        crop_potential_evapotranspiration: (mm/d) crop potential evapotranspiration
        soil_coefficient: (-) soil coefficient

    Returns:
        (mm/d) actual crop evapotranspiration

    Holos source code:
        https://github.com/holos-aafc/Holos/blob/8a3d8fb047c2058a3dbe273f5a8550ae63a54f14/H.Core/Calculators/Climate/ClimateParameterCalculator.cs#L762
    """
    return soil_coefficient * crop_potential_evapotranspiration
