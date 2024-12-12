from holos_service.common import EnumGeneric
from holos_service.components.animals.common import (AnimalType)


class GroupNames(EnumGeneric):
    bulls: str = "Bulls"
    replacement_heifers: str = "Replacement heifers"
    cows: str = "Cows"
    calves: str = "Calves"


class GroupTypes(EnumGeneric):
    beef: str = AnimalType.beef.value  # "Beef"
    beef_backgrounder: str = AnimalType.beef_backgrounder.value  # "BeefBackgrounder"
    beef_backgrounder_heifer: str = AnimalType.beef_backgrounder_heifer.value  # "BeefBackgrounderHeifer"
    beef_backgrounder_steer: str = AnimalType.beef_backgrounder_steer.value  # "BeefBackgrounderSteer"
    beef_bulls: str = AnimalType.beef_bulls.value  # "BeefBulls"
    beef_calf: str = AnimalType.beef_calf.value  # "BeefCalf"
    beef_cow: str = AnimalType.beef_cow.value  # "BeefCow"
    beef_cow_dry: str = AnimalType.beef_cow_dry.value  # "BeefCowDry"
    beef_cow_lactating: str = AnimalType.beef_cow_lactating.value  # "BeefCowLactating"
    beef_finisher: str = AnimalType.beef_finisher.value  # "BeefFinisher"
    beef_finishing_heifer: str = AnimalType.beef_finishing_heifer.value  # "BeefFinishingHeifer"
    beef_finishing_steer: str = AnimalType.beef_finishing_steer.value  # "BeefFinishingSteer"
    beef_replacement_heifers: str = AnimalType.beef_replacement_heifers.value  # "BeefReplacementHeifers"
