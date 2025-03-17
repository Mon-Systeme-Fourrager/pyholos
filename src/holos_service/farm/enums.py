from enum import StrEnum, auto


class YieldAssignmentMethod(StrEnum):
    """Used to lookup default yields for a particular year and crop type.

    Holos source code:
        https://github.com/holos-aafc/Holos/blob/768b3d8fe2565dad0ba01fb8490974f1047a114f/H.Core/Enumerations/YieldAssignmentMethod.cs#L6
    """
    Average = auto()
    """Takes the average of the yields from the crop view items of the field component"""

    Custom = auto()
    """Uses the values entered for each year (by the user on the details screen)"""

    CARValue = auto()
    """Uses CAR region values"""

    InputFile = auto()
    """Reads a yield input file from the user"""

    InputFileThenAverage = auto()
    """Reads a yield input file from the user and the use the average of all crops in rotation"""

    SmallAreaData = auto()
    """Use Small Area Data (SAD) yields (https://open.canada.ca/data/en/dataset/65f1cde1-95e0-4a1d-9a1a-c45b2f83a351)"""


class CarbonModellingStrategies(StrEnum):
    """
    Holos source code:
        https://github.com/holos-aafc/Holos/blob/768b3d8fe2565dad0ba01fb8490974f1047a114f/H.Core/Enumerations/CarbonModellingStrategies.cs#L11
    """
    IPCCTier2 = auto()
    ICBM = auto()
