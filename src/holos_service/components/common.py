from enum import StrEnum, unique, auto

from holos_service.common import EnumGeneric


@unique
class ComponentCategory(StrEnum):
    LandManagement = auto()
    BeefProduction = auto()
    Dairy = auto()
    Swine = auto()
    Poultry = auto()
    OtherLivestock = auto()
    Sheep = auto()
    Infrastructure = auto()


class ComponentType(EnumGeneric):
    """Holos component types

    References:
        Source code: https://github.com/holos-aafc/Holos/blob/396f1ab9bc7247e6d78766f9445c14d2eb7c0d9d/H.Core/Models/ComponentType.cs#L5

    """
    rotation: str = "Rotation"
    pasture: str = "Pasture"
    range: str = "Range"
    shelterbelt: str = "Shelterbelt"
    field: str = "Field"
    cow_calf: str = "CowCalf"
    backgrounding: str = "Backgrounding"
    finishing: str = "Finishing"
    grassland: str = "Grassland"
    dairy: str = "Dairy"
    dairy_lactating: str = "DairyLactating"
    dairy_heifer: str = "DairyHeifer"
    dairy_dry: str = "DairyDry"
    dairy_calf: str = "DairyCalf"
    dairy_bulls: str = "DairyBulls"
    swine: str = "Swine"
    boar: str = "Boar"
    swine_finishers: str = "SwineFinishers"
    swine_starters: str = "SwineStarters"
    swine_lactating_sows: str = "SwineLactatingSows"
    swine_dry_sows: str = "SwineDrySows"
    swine_growers: str = "SwineGrowers"
    poultry: str = "Poultry"
    poultry_layers_wet: str = "PoultryLayersWet"
    poultry_turkeys: str = "PoultryTurkeys"
    poultry_geese: str = "PoultryGeese"
    poultry_broilers: str = "PoultryBroilers"
    poultry_ducks: str = "PoultryDucks"
    poultry_layers_dry: str = "PoultryLayersDry"
    sheep: str = "Sheep"
    sheep_feedlot: str = "SheepFeedlot"
    rams: str = "Rams"
    lambs_and_ewes: str = "LambsAndEwes"
    ewes_and_lambs: str = "EwesAndLambs" # added to the original code for convenience
    other_livestock: str = "OtherLivestock"
    alpaca: str = "Alpaca"
    elk: str = "Elk"
    goats: str = "Goats"
    deer: str = "Deer"
    horses: str = "Horses"
    mules: str = "Mules"
    bison: str = "Bison"
    llamas: str = "Llamas"
    farrow_to_wean: str = "FarrowToWean"
    iso_wean: str = "IsoWean"
    farrow_to_finish: str = "FarrowToFinish"
    chicken_pullet_farm: str = "ChickenPulletFarm"
    chicken_multiplier_breeder: str = "ChickenMultiplierBreeder"
    chicken_meat_production: str = "ChickenMeatProduction"
    turkey_multiplier_breeder: str = "TurkeyMultiplierBreeder"
    turkey_meat_production: str = "TurkeyMeatProduction"
    chicken_egg_production: str = "ChickenEggProduction"
    chicken_multiplier_hatchery: str = "ChickenMultiplierHatchery"
    anaerobic_digestion: str = "AnaerobicDigestion"

    def to_str(self):
        return f'{self.value}Component'


def calculate_fraction_of_nitrogen_lost_by_leaching_and_runoff(
        growing_season_precipitation: float,
        growing_season_evapotranspiration: float
) -> float:
    """Calculates the nitrogen loss due to leaching and runoff

    Args:
        growing_season_precipitation: Growing season precipitation, by ecodistrict (May – October)</param>
        growing_season_evapotranspiration: Growing season potential evapotranspiration, by ecodistrict (May – October)

    Returns:
        (kg N (kg N)^-1) fraction of N lost by leaching and runoff

    Holos Source Code:
        https://github.com/RamiALBASHA/Holos/blob/71638efd97c84c6ded45e342ce664477df6f803f/H.Core/Calculators/Nitrogen/NitrogenInputCalculatorBase.cs#L15

    """
    fraction_of_nitrogen_lost_by_leaching_and_runoff = 0.3247 * (
            growing_season_precipitation / growing_season_evapotranspiration) - 0.0247
    return min(0.3, max(0.05, fraction_of_nitrogen_lost_by_leaching_and_runoff))
