from holos_service.common import EnumGeneric
from holos_service.common import EnumGeneric, HolosVar
from holos_service.config import PathsHolosResources
from holos_service.utils import read_holos_resource_table


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


class Bedding:
    def __init__(
            self,
            housing_type: HousingType,
            bedding_material_type: BeddingMaterialType | None,
            animal_type: AnimalType,
            total_carbon_kilograms_dry_matter_for_bedding: float = None,
            total_nitrogen_kilograms_dry_matter_for_bedding: float = None,
            moisture_content_of_bedding_material: float = None
    ):
        default_bedding_material_composition = self.get_bedding_material_composition(
            bedding_material_type=bedding_material_type,
            animal_type=animal_type)

        if total_carbon_kilograms_dry_matter_for_bedding is None:
            total_carbon_kilograms_dry_matter_for_bedding = default_bedding_material_composition[
                'TotalCarbonKilogramsDryMatter']
        if total_nitrogen_kilograms_dry_matter_for_bedding is None:
            total_nitrogen_kilograms_dry_matter_for_bedding = default_bedding_material_composition[
                'TotalNitrogenKilogramsDryMatter']
        if moisture_content_of_bedding_material is None:
            moisture_content_of_bedding_material = default_bedding_material_composition['MoistureContent']

        self.user_defined_bedding_rate = HolosVar(
            name='User Defined Bedding Rate',
            value=self.get_default_bedding_rate(
                housing_type=housing_type,
                bedding_material_type=bedding_material_type,
                animal_type=animal_type))
        self.total_carbon_kilograms_dry_matter_for_bedding = HolosVar(
            name='Total Carbon Kilograms Dry Matter For Bedding',
            value=total_carbon_kilograms_dry_matter_for_bedding)
        self.total_nitrogen_kilograms_dry_matter_for_bedding = HolosVar(
            name='Total Nitrogen Kilograms Dry Matter For Bedding',
            value=total_nitrogen_kilograms_dry_matter_for_bedding)
        self.moisture_content_of_bedding_material = HolosVar(
            name='Moisture Content Of Bedding Material',
            value=moisture_content_of_bedding_material)

    @staticmethod
    def get_default_bedding_rate(
            housing_type: HousingType,
            bedding_material_type: BeddingMaterialType,
            animal_type: AnimalType
    ) -> int | float:
        # https://github.com/holos-aafc/Holos/blob/53f778f9bd4579d164de10f5b04db34d020b96a9/H.Core/Providers/Animals/Table_30_Default_Bedding_Material_Composition_Provider.cs#L301
        _housing_type = HousingTypeExtensions(housing_type=housing_type)
        _animal_type = AnimalTypeExtensions(animal_type=animal_type)


        if _housing_type.is_pasture:
            return 0

        if _animal_type.is_young_type:
            return 0

        if _animal_type.is_beef_cattle_type:
            if bedding_material_type == BeddingMaterialType.straw:
                if _housing_type.is_feed_lot:
                    return 1.5

                if _housing_type.is_barn:
                    return 3.5

            if bedding_material_type == BeddingMaterialType.wood_chip:
                if _housing_type.is_feed_lot:
                    return 3.6

                if _housing_type.is_barn:
                    return 5.0

        if _animal_type.is_dairy_cattle_type:
            # Currently, all housing types have same rates for bedding types
            if any([
                _housing_type.is_tie_stall,
                _housing_type.is_free_stall,
                housing_type == HousingType.dry_lot]):
                if bedding_material_type == BeddingMaterialType.sand:
                    return 24.3

                if bedding_material_type == BeddingMaterialType.separated_manure_solid:
                    return 0

                if bedding_material_type == BeddingMaterialType.straw_long:
                    return 0.7

                if bedding_material_type == BeddingMaterialType.straw_chopped:
                    return 0.7

                if bedding_material_type == BeddingMaterialType.shavings:
                    return 2.1

                if bedding_material_type == BeddingMaterialType.sawdust:
                    return 2.1

        # Footnote 8 for sheep value reference.
        if _animal_type.is_sheep_type:
            return 0.57

        if _animal_type.is_swine_type:
            if bedding_material_type == BeddingMaterialType.straw_long:
                return 0.70
            else:
                return 0.79

        if _animal_type.is_poultry_type:
            if any([
                bedding_material_type == BeddingMaterialType.sawdust,
                bedding_material_type == BeddingMaterialType.straw,
                bedding_material_type == BeddingMaterialType.shavings]):
                if animal_type == AnimalType.broilers:
                    return 0.0014

                if animal_type == AnimalType.chicken_pullets:
                    return 0.0014

                if any([
                    animal_type == AnimalType.layers,
                    animal_type == AnimalType.chicken_hens]):
                    return 0.0028

                if _animal_type.is_turkey_type:
                    return 0.011

                else:
                    return 0
            else:
                return 0

        if _animal_type.is_other_animal_type:
            # Footnote 11 for Other livestock value reference
            match animal_type:
                case AnimalType.llamas:
                    return 0.57

                case AnimalType.alpacas:
                    return 0.57

                case AnimalType.deer:
                    return 1.5

                case AnimalType.elk:
                    return 1.5

                case AnimalType.goats:
                    return 0.57

                case AnimalType.horses:
                    return 1.5

                case AnimalType.mules:
                    return 1.5

                case AnimalType.bison:
                    return 1.5

                # added here since the original case statement in C# does not cover all possibilities
                case _:
                    return 1
        else:
            return 1

        pass

    @staticmethod
    def get_bedding_material_composition(
            bedding_material_type: BeddingMaterialType,
            animal_type: AnimalType
    ) -> dict:
        _animal_type = AnimalTypeExtensions(animal_type=animal_type)
        if _animal_type.is_beef_cattle_type:
            animal_lookup_type = AnimalType.beef
        elif _animal_type.is_dairy_cattle_type:
            animal_lookup_type = AnimalType.dairy
        elif _animal_type.is_sheep_type:
            animal_lookup_type = AnimalType.sheep
        elif _animal_type.is_swine_type:
            animal_lookup_type = AnimalType.swine
        elif _animal_type.is_poultry_type:
            animal_lookup_type = AnimalType.poultry
        else:
            # Other animals have a value for animal group (Horses, Goats, etc.)
            animal_lookup_type = animal_type

        df = read_holos_resource_table(
            path_file=PathsHolosResources.Table_30_Default_Bedding_Material_Composition_Provider)

        result = df[
            (df['BeddingMaterial'] == bedding_material_type) &
            (df['AnimalType'] == animal_lookup_type.value)]

        if not result.empty:
            return result.iloc[0].to_dict()
        else:
            # Trace.TraceError($"{nameof(Farm)}.{nameof(GetBeddingMaterialComposition)}: unable to return bedding material data for {animalType.GetDescription()}, and {beddingMaterialType.GetHashCode()}. Returning default value of 1.");

            # return new Table_30_Default_Bedding_Material_Composition_Data();
            return {k: None for k in result.columns}
