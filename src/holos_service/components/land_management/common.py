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


