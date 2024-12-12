from holos_service.common import EnumGeneric


class GroupNames(EnumGeneric):
    bulls: str = "Bulls"
    replacement_heifers: str = "Replacement heifers"
    cows: str = "Cows"
    calves: str = "Calves"
