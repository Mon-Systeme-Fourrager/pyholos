from holos_service.common import EnumGeneric


class ComponentCategory(EnumGeneric):
    land_management: str = "LandManagement"
    beef_production: str = "BeefProduction"
    dairy: str = "Dairy"
    swine: str = "Swine"
    poultry: str = "Poultry"
    other_livestock: str = "OtherLivestock"
    sheep: str = "Sheep"
    infrastructure: str = "Infrastructure"
