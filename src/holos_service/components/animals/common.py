from holos_service.common import EnumGeneric


class AnimalType(EnumGeneric):
    not_selected: str = "NotSelected"
    alpacas: str = "Alpacas"
    beef_backgrounder: str = "BeefBackgrounder"
    beef_backgrounder_steer: str = "BeefBackgrounderSteer"
    beef_backgrounder_heifer: str = "BeefBackgrounderHeifer"
    beef_finishing_steer: str = "BeefFinishingSteer"
    beef_finishing_heifer: str = "BeefFinishingHeifer"
    beef: str = "Beef"
    beef_bulls: str = "BeefBulls"
    beef_calf: str = "BeefCalf"
    beef_cow_lactating: str = "BeefCowLactating"  # This also means 'regular' cows (i.e. non-lactating)
    beef_cow_dry: str = "BeefCowDry"
    beef_finisher: str = "BeefFinisher"  # /// Also known as buffalo
    bison: str = "Bison"
    swine_boar: str = "SwineBoar"
    broilers: str = "Broilers"
    chicken: str = "Chicken"
    cow_calf: str = "CowCalf"
    beef_cow: str = "BeefCow"
    calf: str = "Calf"
    dairy: str = "Dairy"
    dairy_bulls: str = "DairyBulls"
    dairy_dry_cow: str = "DairyDryCow"
    dairy_calves: str = "DairyCalves"
    dairy_heifers: str = "DairyHeifers"
    dairy_lactating_cow: str = "DairyLactatingCow"
    deer: str = "Deer"
    swine_dry_sow: str = "SwineDrySow"
    ducks: str = "Ducks"
    elk: str = "Elk"
    ewes: str = "Ewes"  # Assumption is all ewes are pregnant
    geese: str = "Geese"
    goats: str = "Goats"
    swine_grower: str = "SwineGrower"  # Also known as Hogs
    horses: str = "Horses"
    lambs: str = "Lambs"
    lambs_and_ewes: str = "LambsAndEwes"
    swine_lactating_sow: str = "SwineLactatingSow"
    layers_dry_poultry: str = "LayersDryPoultry"
    layers_wet_poultry: str = "LayersWetPoultry"
    llamas: str = "Llamas"
    mules: str = "Mules"
    other_livestock: str = "OtherLivestock"
    poultry: str = "Poultry"
    beef_replacement_heifers: str = "BeefReplacementHeifers"
    sheep: str = "Sheep"
    ram: str = "Ram"
    weaned_lamb: str = "WeanedLamb"
    sheep_feedlot: str = "SheepFeedlot"
    stockers: str = "Stockers"
    stocker_steers: str = "StockerSteers"
    stocker_heifers: str = "StockerHeifers"
    swine: str = "Swine"
    swine_starter: str = "SwineStarter"
    swine_finisher: str = "SwineFinisher"
    turkeys: str = "Turkeys"
    young_bulls: str = "YoungBulls"
    swine_gilts: str = "SwineGilts"  # Female pigs that have not farrowed a litter. Also known as maiden gilts.
    swine_sows: str = "SwineSows"
    swine_piglets: str = "SwinePiglets"
    chicken_pullets: str = "ChickenPullets"  # Juvenile female
    chicken_cockerels: str = "ChickenCockerels"  # Juvenile male
    chicken_roosters: str = "ChickenRoosters"  # Adult male
    chicken_hens: str = "ChickenHens"  # Adult female
    young_tom: str = "YoungTom"  # Juvenile male turkey
    tom: str = "Tom"  # Adult male turkey
    young_turkey_hen: str = "YoungTurkeyHen"  # Young female turkey
    turkey_hen: str = "TurkeyHen"  # Adult female turkey
    chicken_eggs: str = "ChickenEggs"
    turkey_eggs: str = "TurkeyEggs"
    chicks: str = "Chicks"  # Newly hatched chicken
    poults: str = "Poults"  # Newly hatched turkey
    cattle: str = "Cattle"
    layers: str = "Layers"


class HousingType(EnumGeneric):
    not_selected: str = "NotSelected"
    confined_no_barn: str = "ConfinedNoBarn"
    """Also known as 'Confined no barn (feedlot)'
    """
    housed_in_barn: str = "HousedInBarn"
    housed_ewes: str = "HousedEwes"
    housed_in_barn_solid: str = "HousedInBarnSolid"
    housed_in_barn_slurry: str = "HousedInBarnSlurry"
    enclosed_pasture: str = "EnclosedPasture"
    open_range_or_hills: str = "OpenRangeOrHills"
    tie_stall: str = "TieStall"
    small_free_stall: str = "SmallFreeStall"
    large_free_stall: str = "LargeFreeStall"
    grazing_under3km: str = "GrazingUnder3km"
    grazing_over3km: str = "GrazingOver3km"
    confined: str = "Confined"
    flat_pasture: str = "FlatPasture"
    hilly_pasture_or_open_range: str = "HillyPastureOrOpenRange"
    pasture: str = "Pasture"
    """Pasture, range, or paddock
    """
    dry_lot: str = "DryLot"
    """Also known as 'Standing or exercise yard'
    """
    swath_grazing: str = "SwathGrazing"
    custom: str = "Custom"
    free_stall_barn_solid_litter: str = "FreeStallBarnSolidLitter"
    free_stall_barn_slurry_scraping: str = "FreeStallBarnSlurryScraping"
    free_stall_barn_flushing: str = "FreeStallBarnFlushing"
    free_stall_barn_milk_parlour_slurry_flushing: str = "FreeStallBarnMilkParlourSlurryFlushing"
    """Also known as 'Milking parlour (slurry - flushing)'
    """
    tie_stall_solid_litter: str = "TieStallSolidLitter"
    """Also known as 'Tie-stall barn (solid)'
    """
    tie_stall_slurry: str = "TieStallSlurry"
    """Also known as 'Tie-stall barn (slurry)'
    """


class HousingTypeExtensions:
    def __init__(
            self,
            housing_type: HousingType
    ):
        # https://github.com/holos-aafc/Holos/blob/53f778f9bd4579d164de10f5b04db34d020b96a9/H.Core/Enumerations/HousingTypeExtensions.cs#L10
        self.is_free_stall = any([housing_type == v for v in (
            housing_type.small_free_stall,
            housing_type.large_free_stall,
            housing_type.free_stall_barn_flushing,
            housing_type.free_stall_barn_milk_parlour_slurry_flushing,
            housing_type.free_stall_barn_slurry_scraping,
            housing_type.free_stall_barn_solid_litter)])

        self.is_tie_stall = any([housing_type == v for v in (
            housing_type.tie_stall,
            housing_type.tie_stall_slurry,
            housing_type.tie_stall_solid_litter)])

        self.is_barn = any([housing_type == v for v in (
            housing_type.housed_in_barn,
            housing_type.housed_in_barn_slurry,
            housing_type.housed_in_barn_solid)])

        self.is_feed_lot = any([housing_type == v for v in (
            housing_type.confined,
            housing_type.confined_no_barn)])

        self.is_electrical_consuming_housing_type = any([
            self.is_free_stall,
            self.is_barn,
            self.is_tie_stall,
            self.is_feed_lot])

        self.is_indoor_housing = any([housing_type == v for v in (
            housing_type.housed_in_barn,
            housing_type.housed_in_barn_slurry,
            housing_type.housed_in_barn_solid,
            housing_type.free_stall_barn_flushing,
            housing_type.free_stall_barn_solid_litter,
            housing_type.free_stall_barn_slurry_scraping,
            housing_type.free_stall_barn_milk_parlour_slurry_flushing)])

        self.is_pasture = any([housing_type == v for v in (
            housing_type.pasture,
            housing_type.enclosed_pasture,
            housing_type.flat_pasture,
            housing_type.grazing_over3km,
            housing_type.grazing_under3km,
            housing_type.hilly_pasture_or_open_range,
            housing_type.open_range_or_hills,
            housing_type.swath_grazing)])


class BeddingMaterialType(EnumGeneric):
    straw: str = 'Straw'
    wood_chip: str = 'WoodChip'
    separated_manure_solid: str = 'SeparatedManureSolid'
    sand: str = 'Sand'
    straw_long: str = 'StrawLong'
    straw_chopped: str = 'StrawChopped'
    shavings: str = 'Shavings'
    sawdust: str = 'Sawdust'
    paper_products: str = 'PaperProducts'
    peat: str = 'Peat'
    hemp: str = 'Hemp'

    @classmethod
    def get_value(cls, name: str | None):
        return "None" if name is None else getattr(cls, name).value
