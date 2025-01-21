from enum import Enum

class Defaults(Enum):
    EmissionFactorForLeachingAndRunoff = 0.011 # Updated to IPCC 2019 value
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


