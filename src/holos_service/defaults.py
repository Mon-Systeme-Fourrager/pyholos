class Defaults:
    EmissionFactorForLeachingAndRunoff = 0.011  # Updated to IPCC 2019 value
    """(kg(N2O-N) kg(N)-1) emission factor for leaching and runoff"""

    PercentageOfProductReturnedToSoilForPerennials = 35
    """(%) percentage of the perennial crops biomass returned to soil after harvest"""

    PercentageOfRootsReturnedToSoilForPerennials = 100
    """(%) percentage of the perennial crops root biomass returned to soil after harvest"""

    PercentageOfProductReturnedToSoilForAnnuals = 2
    """(%) percentage of the annual crops biomass returned to soil after harvest"""

    PercentageOfRootsReturnedToSoilForAnnuals = 100
    """(%) percentage of the annual crops root biomass returned to soil after harvest"""

    PercentageOfStrawReturnedToSoilForAnnuals = 100
    """(%) percentage of the annual crops straw biomass returned to soil after harvest"""

    PercentageOfProductReturnedToSoilForRootCrops = 0
    """(%) percentage of the root crops biomass returned to soil after harvest"""

    PercentageOfStrawReturnedToSoilForRootCrops = 100
    """(%) percentage of the root crops straw biomass returned to soil after harvest"""

    # for annual crops
    EmergenceDay = 141
    """(julian day) day of plant emergence for annual crops"""

    RipeningDay = 197
    """(julian day) day of plant ripening for annual crops"""

    Variance = 300
    """width of distribution function for annual crops"""

    # for perennial crops
    EmergenceDayForPerennials = 75
    """(julian day) day of plant emergence for perennial crops"""

    RipeningDayForPerennials = 300
    """(julian day) day of plant ripening for perennial crops"""

    VarianceForPerennials = 1500
    """width of distribution function for perennial crops"""

    # for all crops
    Alfa = 0.7
    """(-) minimum water storage fraction of wilting_point"""

    DecompositionMinimumTemperature = -3.78
    """(degree Celsius) maximum cardinal temperature for decomposition"""

    DecompositionMaximumTemperature = 30
    """(degree Celsius) minimum cardinal temperature for decomposition"""

    MoistureResponseFunctionAtWiltingPoint = 0.18
    """(mm3/mm3) soil volumetric water content at reference wilting point"""

    MoistureResponseFunctionAtSaturation = 0.42
    """(mm3/mm3) soil volumetric water content at reference saturation"""

