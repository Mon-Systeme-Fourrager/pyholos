from holos_service.common import EnumGeneric, HolosVar
from holos_service.components.common import ComponentCategory
from holos_service.config import PathsHolosResources
from holos_service.utils import read_holos_resource_table


class DietAdditiveType(EnumGeneric):
    two_percent_fat: str = "TwoPercentFat"
    four_percent_fat: str = "FourPercentFat"
    five_percent_fat: str = "FivePercentFat"
    ionophore: str = "Inonophore"
    ionophore_plus_two_percent_fat: str = "InonophorePlusTwoPercentFat"
    ionophore_plus_four_percent_fat: str = "InonophorePlusFourPercentFat"
    ionophore_plus_five_percent_fat: str = "IonophorePlusFivePercentFat"
    custom: str = "Custom"

    @classmethod
    def get_value(cls, member: str | None):
        return "None" if member is None else getattr(cls, member).value


class ProductionStage(EnumGeneric):
    gestating: str = "Gestating"
    """Animals that are pregnant.
    """

    lactating: str = "Lactating"
    """Animals that are lactating. Also known as farrowing in swine systems.
    """

    open: str = "Open"
    """Animals that are neither lactating or pregnant.
    """

    weaning: str = "Weaning"
    """Animals that have not been weaned yet.
    """

    growing_and_finishing: str = "GrowingAndFinishing"
    """Animals that have not been weaned yet.
    """

    breeding_stock: str = "BreedingStock"
    """Animals that are used for breeding (boars, bulls, etc.)
    """

    weaned: str = "Weaned"
    """Animals that have been weaned and are no longer milk fed.
    """


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


class ManureAnimalSourceTypes(EnumGeneric):
    not_selected: str = "NotSelected"
    beef_manure: str = "BeefManure"
    dairy_manure: str = "DairyManure"
    swine_manure: str = "SwineManure"
    poultry_manure: str = "PoultryManure"
    sheep_manure: str = "SheepManure"
    other_livestock_manure: str = "OtherLivestockManure"


class AnimalTypeExtensions:
    def __init__(
            self,
            animal_type: AnimalType
    ):
        self.is_young_type = any([animal_type == v for v in (
            animal_type.beef_calf,
            animal_type.dairy_calves,
            animal_type.swine_piglets,
            animal_type.weaned_lamb,
            animal_type.lambs)])

        self.is_beef_cattle_type = any([animal_type == v for v in (
            animal_type.beef,
            animal_type.beef_backgrounder,
            animal_type.beef_bulls,
            animal_type.beef_backgrounder_heifer,
            animal_type.beef_finishing_steer,
            animal_type.beef_finishing_heifer,
            animal_type.beef_replacement_heifers,
            animal_type.beef_finisher,
            animal_type.beef_backgrounder_steer,
            animal_type.beef_calf,
            animal_type.stockers,
            animal_type.stocker_heifers,
            animal_type.stocker_steers,
            animal_type.beef_cow_lactating,
            animal_type.beef_cow,
            animal_type.beef_cow_dry)])

        self.is_dairy_cattle_type = any([animal_type == v for v in (
            animal_type.dairy,
            animal_type.dairy_lactating_cow,
            animal_type.dairy_bulls,
            animal_type.dairy_calves,
            animal_type.dairy_dry_cow,
            animal_type.dairy_heifers)])

        self.is_swine_type = any([animal_type == v for v in (
            animal_type.swine,
            animal_type.swine_finisher,
            animal_type.swine_starter,
            animal_type.swine_lactating_sow,
            animal_type.swine_dry_sow,
            animal_type.swine_grower,
            animal_type.swine_sows,
            animal_type.swine_boar,
            animal_type.swine_gilts,
            animal_type.swine_piglets)])

        self.is_sheep_type = any([animal_type == v for v in (
            animal_type.sheep,
            animal_type.lambs_and_ewes,
            animal_type.ram,
            animal_type.weaned_lamb,
            animal_type.lambs,
            animal_type.ewes,
            animal_type.sheep_feedlot)])

        self.is_poultry_type = any([animal_type == v for v in (
            animal_type.poultry,
            animal_type.layers_wet_poultry,
            animal_type.layers_dry_poultry,
            animal_type.layers,
            animal_type.broilers,
            animal_type.turkeys,
            animal_type.ducks,
            animal_type.geese,
            animal_type.chicken_pullets,
            animal_type.chicken_cockerels,
            animal_type.chicken_roosters,
            animal_type.chicken_hens,
            animal_type.young_tom,
            animal_type.tom,
            animal_type.young_turkey_hen,
            animal_type.turkey_hen,
            animal_type.chicken_eggs,
            animal_type.turkey_eggs,
            animal_type.chicks,
            animal_type.poults)])

        self.is_other_animal_type = any([animal_type == v for v in (
            animal_type.other_livestock,
            animal_type.goats,
            animal_type.alpacas,
            animal_type.deer,
            animal_type.elk,
            animal_type.llamas,
            animal_type.horses,
            animal_type.mules,
            animal_type.bison)])

        self.is_chicken_type = any([animal_type == v for v in (
            animal_type.chicken,
            animal_type.chicken_hens,
            animal_type.layers,
            animal_type.broilers,
            animal_type.chicken_roosters,
            animal_type.chicken_pullets,
            animal_type.chicken_cockerels,
            animal_type.chicken_eggs,
            animal_type.chicks)])

        self.is_turkey_type = any([animal_type == v for v in (
            animal_type.turkey_hen,
            animal_type.young_turkey_hen,
            animal_type.tom,
            animal_type.turkey_eggs,
            animal_type.young_tom,
            animal_type.poults)])

        self.is_layers_type = any([animal_type == v for v in (
            animal_type.layers,
            animal_type.layers_dry_poultry,
            animal_type.layers_wet_poultry)])

        self.is_lactating_type = any([animal_type == v for v in (
            animal_type.beef_cow_lactating,
            animal_type.beef_cow,
            animal_type.dairy_lactating_cow,
            animal_type.ewes)])

        self.is_eggs = any([animal_type == v for v in (
            animal_type.chicken_eggs,
            animal_type.turkey_eggs)])

        self.is_newly_hatched_eggs = any([animal_type == v for v in (
            animal_type.poults,
            animal_type.chicks)])

        self.is_pregnant_type = any([animal_type == v for v in (
            animal_type.beef_cow,
            animal_type.beef_cow_lactating,
            animal_type.dairy_lactating_cow,
            animal_type.dairy_dry_cow,
            animal_type.ewes)])

    def get_category(self):
        if self.is_other_animal_type:
            res = AnimalType.other_livestock

        elif self.is_poultry_type:
            res = AnimalType.poultry

        elif self.is_sheep_type:
            res = AnimalType.sheep

        elif self.is_swine_type:
            res = AnimalType.swine

        elif self.is_dairy_cattle_type:
            res = AnimalType.dairy

        elif self.is_beef_cattle_type:
            res = AnimalType.beef

        else:
            res = AnimalType.not_selected

        return res

    def get_component_category_from_animal_type(self):
        if self.is_beef_cattle_type:
            res = ComponentCategory.beef_production

        elif self.is_dairy_cattle_type:
            res = ComponentCategory.dairy

        elif self.is_swine_type:
            res = ComponentCategory.swine

        elif self.is_poultry_type:
            res = ComponentCategory.poultry

        elif self.is_sheep_type:
            res = ComponentCategory.sheep

        else:
            res = ComponentCategory.other_livestock

        return res

    def get_manure_animal_source(self):
        if self.is_beef_cattle_type:
            res = ManureAnimalSourceTypes.beef_manure

        elif self.is_dairy_cattle_type:
            res = ManureAnimalSourceTypes.dairy_manure

        elif self.is_swine_type:
            res = ManureAnimalSourceTypes.swine_manure

        elif self.is_poultry_type:
            res = ManureAnimalSourceTypes.poultry_manure

        elif self.is_sheep_type:
            res = ManureAnimalSourceTypes.sheep_manure

        else:
            res = ManureAnimalSourceTypes.other_livestock_manure

        return res


class Milk:
    def __init__(
            self,
            production_amount: float = 0,
            fat_content: float = 4,
            protein_content_as_percentage: float = 3.5,
    ):
        """Milk production data

        Args:
            production_amount: (kg) average milk production value based on the province and year specified by user
            fat_content: (%) fat content of milk
            protein_content_as_percentage: (%) protein content of milk
        """
        self.production = production_amount
        self.fat_content = fat_content
        self.protein_content_as_percentage = protein_content_as_percentage


class Diet:
    def __init__(
            self,
            crude_protein_percentage: float,
            forage_percentage: float,
            total_digestible_nutrient_percentage: float,
            ash_percentage: float,
            starch_percentage: float,
            fat_percentage: float,
            neutral_detergent_fiber_percentage: float,
            metabolizable_energy: float,
            dietary_net_energy_concentration: float
    ):
        """Diet composition data

        Args:
            crude_protein_percentage: (-) percentage of crude protein in the diet dry matter (between 0 and 100)
            forage_percentage: (-) percentage of forage in the diet dry matter (between 0 and 100)
            total_digestible_nutrient_percentage: (-) percentage of total digestible nutrient in the diet dry matter (between 0 and 100)
            ash_percentage: (-) percentage of ash in the diet dry matter (between 0 and 100)
            starch_percentage: (-) percentage of starch in the diet dry matter (between 0 and 100)
            fat_percentage: (-) percentage of fat in the diet dry matter (between 0 and 100)
            neutral_detergent_fiber_percentage: (-) percentage of neutral detergent fiber in the diet dry matter (between 0 and 100)
            metabolizable_energy: (Mcal kg-1) metabolizable energy of the diet
            dietary_net_energy_concentration: (MJ (kg DM)^-1) dietary net energy concentration
        """
        self.crude_protein_percentage = crude_protein_percentage
        self.forage_percentage = forage_percentage
        self.total_digestible_nutrient_percentage = total_digestible_nutrient_percentage
        self.ash_percentage = ash_percentage
        self.starch_percentage = starch_percentage
        self.fat_percentage = fat_percentage
        self.neutral_detergent_fiber_percentage = neutral_detergent_fiber_percentage
        self.metabolizable_energy = metabolizable_energy
        self.dietary_net_energy_concentration = dietary_net_energy_concentration


# class HousingSystem:
#     def __init__(
#             self,
#             bedding_rate: float,
#             total_carbon_kilograms_dry_matter_for_bedding: float
#     ):
#         """
#
#         Args:
#             bedding_rate: (kg head-1 day-1) rate of bedding material added to the housing system
#             total_carbon_kilograms_dry_matter_for_bedding: (kg(C) kg(DM)-1)
#
#         """
#         self.user_defined_bedding_rate = bedding_rate
#         self.total_carbon_kilograms_dry_matter_for_bedding = total_carbon_kilograms_dry_matter_for_bedding * bedding_rate


# class Table_30_Default_Bedding_Material_Composition_Data(EnumGeneric):
#     ComponentCategory = "ComponentCategory { get; set; }"
#     AnimalType = " AnimalType { get; set; }"
#     ComponentCategoryString: str = "ComponentCategory.GetDescription(); }"
#     BeddingMaterialType = "BeddingMaterial { get; set; }"
#     BeddingMaterialString: str = "BeddingMaterial.GetDescription()"
#     MoistureContent: float  # %
#     TotalNitrogenKilogramsDryMatter: float  # %(kg N/kg DM)
#     TotalCarbonKilogramsDryMatter: float  # (kg C/kg DM)
#     TotalPhosphorusKilogramsDryMatter: double
#     CarbonToNitrogenRatio: float  # (unitless)


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


class AnimalCoefficientData:
    def __init__(
            self,
            baseline_maintenance_coefficient: float = 0,
            gain_coefficient: float = 0,
            default_initial_weight: float = 0,
            default_final_weight: float = 0
    ):
        """Table 16. Livestock coefficients for beef cattle and dairy cattle.

        Args:
            baseline_maintenance_coefficient: (dimensionless?) baseline maintenance coefficient (C_f)
            gain_coefficient: (dimensionless?) gain coefficient (C_d)
            default_initial_weight: (kg) initial weight
            default_final_weight: (kg) final weight
        """
        self.baseline_maintenance_coefficient = baseline_maintenance_coefficient
        self.gain_coefficient = gain_coefficient
        self.default_initial_weight = default_initial_weight
        self.default_final_weight = default_final_weight