from enum import auto

from holos_service.utils import AutoNameEnum


class IrrigationType(AutoNameEnum):
    Irrigated = auto()
    RainFed = auto()


class TillageType(AutoNameEnum):
    """
    Holos Source Code:
        https://github.com/holos-aafc/Holos/blob/b183dab99d211158d1fed9da5370ce599ac7c914/H.Core/Enumerations/TillageType.cs#L6
    """
    NotSelected = auto()
    Reduced = auto()
    NoTill = auto()
    Intensive = auto()


class HarvestMethod(AutoNameEnum):
    """
    Holos source code:
        https://github.com/holos-aafc/Holos/blob/b183dab99d211158d1fed9da5370ce599ac7c914/H.Core/Enumerations/HarvestMethods.cs#L6
    """
    Silage = auto()
    Swathing = auto()
    GreenManure = auto()
    CashCrop = auto()
    StubbleGrazing = auto()
    NONE = auto()  # Used for fallow, etc.


class ManureApplicationTypes(AutoNameEnum):
    """
    Holos source code:
        https://github.com/holos-aafc/Holos/blob/c06f6619907fba89c3ddc29b4239a903a8c20a7a/H.Core/Enumerations/ManureApplicationTypes.cs#L9
    """
    NotSelected = auto()
    OptionA = auto()
    OptionB = auto()
    OptionC = auto()
    TilledLandSolidSpread = auto()  # Also known as 'Solid spread (intensive tillage)
    UntilledLandSolidSpread = auto()  # Also known as 'Solid spread (no tillage or reduced tillage)
    SlurryBroadcasting = auto()
    DropHoseBanding = auto()
    ShallowInjection = auto()
    DeepInjection = auto()


class TimePeriodCategory(AutoNameEnum):
    """
    Holos source code:
        https://github.com/holos-aafc/Holos/blob/c06f6619907fba89c3ddc29b4239a903a8c20a7a/H.Core/Enumerations/TimePeriodCategory.cs#L3C4-L7C16
    """
    Past = auto()
    Current = auto()
    Future = auto()
