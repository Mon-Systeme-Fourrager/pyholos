from holos_service.common import EnumGeneric, HolosVar
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

    def is_young_type(self):
        return self in {
            self.__class__.beef_calf,
            self.__class__.dairy_calves,
            self.__class__.swine_piglets,
            self.__class__.weaned_lamb,
            self.__class__.lambs
        }

    def is_beef_cattle_type(self):
        return self in {
            self.__class__.beef,
            self.__class__.beef_backgrounder,
            self.__class__.beef_bulls,
            self.__class__.beef_backgrounder_heifer,
            self.__class__.beef_finishing_steer,
            self.__class__.beef_finishing_heifer,
            self.__class__.beef_replacement_heifers,
            self.__class__.beef_finisher,
            self.__class__.beef_backgrounder_steer,
            self.__class__.beef_calf,
            self.__class__.stockers,
            self.__class__.stocker_heifers,
            self.__class__.stocker_steers,
            self.__class__.beef_cow_lactating,
            self.__class__.beef_cow,
            self.__class__.beef_cow_dry
        }

    def is_dairy_cattle_type(self):
        return self in {
            self.__class__.dairy,
            self.__class__.dairy_lactating_cow,
            self.__class__.dairy_bulls,
            self.__class__.dairy_calves,
            self.__class__.dairy_dry_cow,
            self.__class__.dairy_heifers
        }

    def is_swine_type(self):
        return self in {
            self.__class__.swine,
            self.__class__.swine_finisher,
            self.__class__.swine_starter,
            self.__class__.swine_lactating_sow,
            self.__class__.swine_dry_sow,
            self.__class__.swine_grower,
            self.__class__.swine_sows,
            self.__class__.swine_boar,
            self.__class__.swine_gilts,
            self.__class__.swine_piglets
        }

    def is_sheep_type(self):
        return self in {
            self.__class__.sheep,
            self.__class__.lambs_and_ewes,
            self.__class__.ram,
            self.__class__.weaned_lamb,
            self.__class__.lambs,
            self.__class__.ewes,
            self.__class__.sheep_feedlot
        }

    def is_poultry_type(self):
        return self in {
            self.__class__.poultry,
            self.__class__.layers_wet_poultry,
            self.__class__.layers_dry_poultry,
            self.__class__.layers,
            self.__class__.broilers,
            self.__class__.turkeys,
            self.__class__.ducks,
            self.__class__.geese,
            self.__class__.chicken_pullets,
            self.__class__.chicken_cockerels,
            self.__class__.chicken_roosters,
            self.__class__.chicken_hens,
            self.__class__.young_tom,
            self.__class__.tom,
            self.__class__.young_turkey_hen,
            self.__class__.turkey_hen,
            self.__class__.chicken_eggs,
            self.__class__.turkey_eggs,
            self.__class__.chicks,
            self.__class__.poults
        }

    def is_other_animal_type(self):
        return self in {
            self.__class__.other_livestock,
            self.__class__.goats,
            self.__class__.alpacas,
            self.__class__.deer,
            self.__class__.elk,
            self.__class__.llamas,
            self.__class__.horses,
            self.__class__.mules,
            self.__class__.bison
        }

    def is_chicken_type(self):
        return self in {
            self.__class__.chicken,
            self.__class__.chicken_hens,
            self.__class__.layers,
            self.__class__.broilers,
            self.__class__.chicken_roosters,
            self.__class__.chicken_pullets,
            self.__class__.chicken_cockerels,
            self.__class__.chicken_eggs,
            self.__class__.chicks
        }

    def is_turkey_type(self):
        return self in {
            self.__class__.turkey_hen,
            self.__class__.young_turkey_hen,
            self.__class__.tom,
            self.__class__.turkey_eggs,
            self.__class__.young_tom,
            self.__class__.poults
        }

    def is_layers_type(self):
        return self in {
            self.__class__.layers,
            self.__class__.layers_dry_poultry,
            self.__class__.layers_wet_poultry
        }

    def is_lactating_type(self):
        return self in {
            self.__class__.beef_cow_lactating,
            self.__class__.beef_cow,
            self.__class__.dairy_lactating_cow,
            self.__class__.ewes
        }

    def is_eggs(self):
        return self in {
            self.__class__.chicken_eggs,
            self.__class__.turkey_eggs
        }

    def is_newly_hatched_eggs(self):
        return self in {
            self.__class__.poults,
            self.__class__.chicks
        }

    def is_pregnant_type(self):
        return self in {
            self.__class__.beef_cow,
            self.__class__.beef_cow_lactating,
            self.__class__.dairy_lactating_cow,
            self.__class__.dairy_dry_cow,
            self.__class__.ewes
        }

    def get_category(self):
        if self.is_other_animal_type():
            res = self.other_livestock

        elif self.is_poultry_type():
            res = self.poultry

        elif self.is_sheep_type():
            res = self.sheep

        elif self.is_swine_type():
            res = self.swine

        elif self.is_dairy_cattle_type():
            res = self.dairy

        elif self.is_beef_cattle_type():
            res = self.beef

        else:
            res = self.not_selected

        return res


class ManureAnimalSourceTypes(EnumGeneric):
    not_selected: str = "NotSelected"
    beef_manure: str = "BeefManure"
    dairy_manure: str = "DairyManure"
    swine_manure: str = "SwineManure"
    poultry_manure: str = "PoultryManure"
    sheep_manure: str = "SheepManure"
    other_livestock_manure: str = "OtherLivestockManure"


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

    # This section corresponds to the HousingTypeExtensions class in the original holos source code
    # https://github.com/holos-aafc/Holos/blob/53f778f9bd4579d164de10f5b04db34d020b96a9/H.Core/Enumerations/HousingTypeExtensions.cs#L10

    def is_free_stall(self):
        return self in {
            self.__class__.small_free_stall,
            self.__class__.large_free_stall,
            self.__class__.free_stall_barn_flushing,
            self.__class__.free_stall_barn_milk_parlour_slurry_flushing,
            self.__class__.free_stall_barn_slurry_scraping,
            self.__class__.free_stall_barn_solid_litter
        }

    def is_tie_stall(self):
        return self in {
            self.__class__.tie_stall,
            self.__class__.tie_stall_slurry,
            self.__class__.tie_stall_solid_litter
        }

    def is_barn(self):
        return self in {
            self.__class__.housed_in_barn,
            self.__class__.housed_in_barn_slurry,
            self.__class__.housed_in_barn_solid
        }

    def is_feed_lot(self):
        return self in {
            self.__class__.confined,
            self.__class__.confined_no_barn
        }

    def is_electrical_consuming_housing_type(self):
        return any([
            self.is_free_stall(),
            self.is_barn(),
            self.is_tie_stall(),
            self.is_feed_lot()])

    def is_indoor_housing(self):
        return self in {
            self.__class__.housed_in_barn,
            self.__class__.housed_in_barn_slurry,
            self.__class__.housed_in_barn_solid,
            self.__class__.free_stall_barn_flushing,
            self.__class__.free_stall_barn_solid_litter,
            self.__class__.free_stall_barn_slurry_scraping,
            self.__class__.free_stall_barn_milk_parlour_slurry_flushing
        }

    def is_pasture(self):
        return self in {
            self.__class__.pasture,
            self.__class__.enclosed_pasture,
            self.__class__.flat_pasture,
            self.__class__.grazing_over3km,
            self.__class__.grazing_under3km,
            self.__class__.hilly_pasture_or_open_range,
            self.__class__.open_range_or_hills,
            self.__class__.swath_grazing
        }


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

        if housing_type.is_pasture():
            return 0

        if animal_type.is_young_type():
            return 0

        if animal_type.is_beef_cattle_type():
            if bedding_material_type == BeddingMaterialType.straw:
                if housing_type.is_feed_lot():
                    return 1.5

                if housing_type.is_barn():
                    return 3.5

            if bedding_material_type == BeddingMaterialType.wood_chip:
                if housing_type.is_feed_lot():
                    return 3.6

                if housing_type.is_barn():
                    return 5.0

        if animal_type.is_dairy_cattle_type():
            # Currently, all housing types have same rates for bedding types
            if any([
                housing_type.is_tie_stall(),
                housing_type.is_free_stall(),
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
        if animal_type.is_sheep_type():
            return 0.57

        if animal_type.is_swine_type():
            if bedding_material_type == BeddingMaterialType.straw_long:
                return 0.70
            else:
                return 0.79

        if animal_type.is_poultry_type():
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

                if animal_type.is_turkey_type():
                    return 0.011

                else:
                    return 0
            else:
                return 0

        if animal_type.is_other_animal_type:
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
        if animal_type.is_beef_cattle_type():
            animal_lookup_type = AnimalType.beef
        elif animal_type.is_dairy_cattle_type():
            animal_lookup_type = AnimalType.dairy
        elif animal_type.is_sheep_type():
            animal_lookup_type = AnimalType.sheep
        elif animal_type.is_swine_type():
            animal_lookup_type = AnimalType.swine
        elif animal_type.is_poultry_type():
            animal_lookup_type = AnimalType.poultry
        else:
            # Other animals have a value for animal group (Horses, Goats, etc.)
            animal_lookup_type = animal_type

        df = read_holos_resource_table(
            path_file=PathsHolosResources.Table_30_Default_Bedding_Material_Composition_Provider)

        result = df[
            (df['BeddingMaterial'] == bedding_material_type.value) &
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


def get_methane_producing_capacity_of_manure(
        animal_type: AnimalType
) -> float:
    """Returns the default methane producing capacity of manure as a function of the animal type

    Args:
        animal_type: animal type object

    Returns:
        (m^3 CH4 kg^-1 VS): Methane producing capacity of manure (B_o)

    References:
        https://github.com/holos-aafc/Holos/blob/396f1ab9bc7247e6d78766f9445c14d2eb7c0d9d/H.Core/Providers/Animals/Table_35_Methane_Producing_Capacity_Default_Values_Provider.cs#L15

    """
    # Table 35. Default values for maximum methane producing capacity (Bo).
    # <para>Source: IPCC (2019), Table 10.16</para>
    # Footnote 3 : For Methane producing capacity (B0) value reference.

    if animal_type.is_beef_cattle_type():
        res = 0.19

    elif animal_type.is_dairy_cattle_type():
        res = 0.24

    elif animal_type.is_swine_type():
        res = 0.48

    elif animal_type.is_sheep_type():
        res = 0.19

    elif any([
        animal_type == AnimalType.chicken_roosters,
        animal_type == AnimalType.broilers
    ]):
        # Used for broilers from algorithm document
        res = 0.36

    elif any((
            animal_type == AnimalType.chicken_hens,
            animal_type == AnimalType.chicken_pullets,
            animal_type == AnimalType.chicken_cockerels,
            animal_type == AnimalType.layers
    )):
        # Used for layers (wet/dry) from algorithm document
        res = 0.39

    elif animal_type == AnimalType.goats:
        res = 0.18

    elif animal_type == AnimalType.horses:
        res = 0.30

    elif animal_type == AnimalType.mules:
        res = 0.33

    # Footnote 2
    elif any((
            animal_type == AnimalType.llamas,
            animal_type == AnimalType.alpacas
    )):
        res = 0.19

    # Footnote 1
    elif animal_type == AnimalType.bison:
        res = 0.10

    else:
        res = 0

    # Footnote 1: Value for non-dairy cattle used
    # Footnote 2: Value for sheep used
    # Footnote 3: For all animals on pasture, range or paddock, the Bo should be set to 0.19

    return res


def get_default_methane_producing_capacity_of_manure(
        is_pasture: bool,
        animal_type: AnimalType
) -> float:
    """Returns the default methane producing capacity of manure.

    Args:
        is_pasture: True if the housing type is pasture, otherwise False
        animal_type: animal type class

    Returns:
        (m^3 CH4 kg^-1 VS): Methane producing capacity of manure (B_o)

    Notes:
        When housed on pasture, this value should be set to a constant.
        See table 38 "Default values (in Holos source code) for maximum methane producing capacity (Bo)" footnote 3.

    References:
        https://github.com/holos-aafc/Holos/blob/396f1ab9bc7247e6d78766f9445c14d2eb7c0d9d/H.Core/Services/Initialization/Animals/AnimalInitializationService.Methane.cs#L89
    """
    return 0.19 if is_pasture else get_methane_producing_capacity_of_manure(animal_type=animal_type)


class FractionOfOrganicNitrogenMineralizedData:
    def __init__(
            self,
            fraction_immobilized: float | None = None,
            fraction_mineralized: float | None = None,
            fraction_nitrified: float | None = None,
            fraction_denitrified: float | None = None,
            n2o_n: float | None = None,
            no_n: float | None = None,
            n2_n: float | None = None,
            n_leached: float | None = None,
    ):
        """Mineralization of organic N (fecal N and bedding N)

        Args:
            fraction_mineralized: (dimensionless) fraction of nitrogen mineralized
            fraction_immobilized: (dimensionless) fraction of nitrogen immobilized
            fraction_nitrified: (dimensionless) fraction of nitrogen nitrified
            fraction_denitrified: (dimensionless) fraction of nitrogen denitrified
            n2o_n:
            no_n:
            n2_n:
            n_leached:
        """
        self.fraction_mineralized = fraction_immobilized
        self.fraction_immobilized = fraction_mineralized
        self.fraction_nitrified = fraction_nitrified
        self.fraction_denitrified = fraction_denitrified
        self.n2o_n = n2o_n
        self.no_n = no_n
        self.n2_n = n2_n
        self.n_leached = n_leached

    def __eq__(self, other):
        return self.__dict__ == other.__dict__ if isinstance(other, self.__class__) else False


class ManureStateType(EnumGeneric):
    not_selected: str = "NotSelected"
    anaerobic_digester: str = "AnaerobicDigester"
    composted: str = "Composted"
    compost_intensive: str = "CompostIntensive"  # Also known as 'compost - intensive windrow'
    compost_passive: str = "CompostPassive"  # Also known as 'compost - passive windrow'
    daily_spread: str = "DailySpread"
    deep_bedding: str = "DeepBedding"
    deep_pit: str = "DeepPit"  # Also known as 'Deep pit under barn'
    liquid: str = "Liquid"
    liquid_crust: str = "LiquidCrust"  # [Obsolete]
    liquid_separated: str = "LiquidSeparated"  # [Obsolete]
    liquid_no_crust: str = "LiquidNoCrust"  # Also known as 'Liquid/Slurry with no natural crust'
    pasture: str = "Pasture"
    range: str = "Range"
    paddock: str = "Paddock"
    solid: str = "Solid"
    slurry: str = "Slurry"  # [Obsolete]
    slurry_with_natural_crust: str = "SlurryWithNaturalCrust"  # [Obsolete]
    slurry_without_natural_crust: str = "SlurryWithoutNaturalCrust"  # [Obsolete]
    solid_storage: str = "SolidStorage"  # Also known as 'Solid storage (stockpiled)'
    custom: str = "Custom"
    pit_lagoon_no_cover: str = "PitLagoonNoCover"  # [Obsolete]
    liquid_with_natural_crust: str = "LiquidWithNaturalCrust"  # Also known as 'Liquid/Slurry with natural crust'
    liquid_with_solid_cover: str = "LiquidWithSolidCover"  # Also known as Liquid/Slurry with solid cover
    composted_in_vessel: str = "CompostedInVessel"  # (Swine system)
    solid_storage_with_or_without_litter: str = "SolidStorageWithOrWithoutLitter"  # (Poultry system) No different than 'Solid Storage' but poultry solid storage needs the term 'litter' which is incorrect to use in the case of cattle 'Solid Storage' since there is no 'litter' only 'bedding' when considering the cattle system


def get_fraction_of_organic_nitrogen_mineralized_data(
        state_type: ManureStateType,
        animal_type: AnimalType,
        fraction_of_tan_in_liquid_manure_storage_system: float = 1
) -> FractionOfOrganicNitrogenMineralizedData:
    """Table 44. Fraction of organic N mineralized as TAN and the fraction of TAN immobilized to organic N and nitrified
    and denitrified during solid and liquid manure storage for beef and dairy cattle (based on TAN content)
    (Chai et al., 2014,2016).

    Args:
        state_type: manure handling system type
        animal_type: animal type
        fraction_of_tan_in_liquid_manure_storage_system: (-) fraction of excreted N in animal urine (cf. Note 4)

    Returns:


    Notes:
        1. Mineralization of organic N (fecal N and bedding N)
        2. Solid manure composted for ≥ 10 months; data from Chai et al. (2014); these values are used for compost passive and compost intensive beef and dairy cattle manure
        3. Solid manure stockpiled for ≥ 4 months; data from Chai et al. (2014); these values are also used for deep bedding beef and dairy cattle manure
        4. FracurinaryN is the fraction of TAN in the liquid manure storage system (includes liquid/slurry with natural crust, liquid/slurry with no natural crust, liquid/slurry with solid cover and deep pit under barn).
        5. Nitrification of TAN in liquid manure with natural crust (formed from manure, bedding, or waste forage) was considered since the natural crust can be assumed as similar to solid manure (stockpile) in terms of being aerobic. The N2O-N emission factor for liquid manure with a natural crust is 0.005 of total N IPCC (2006), which can be expressed as the TAN based EFs
        6. Nitrification of TAN in liquid manure with no natural crust is assumed to be zero because of anaerobic conditions
        7. All nitrified TAN (nitrate-N) was assumed to be denitrified (no leaching, runoff) in liquid systems.
    """
    if animal_type.is_beef_cattle_type():
        # FracMineralized = Note 1.
        match state_type:
            # // Solid-compost - beef
            # // Note 2
            case ManureStateType.compost_intensive | ManureStateType.compost_passive:
                return FractionOfOrganicNitrogenMineralizedData(
                    fraction_immobilized=0,
                    fraction_mineralized=0.46,
                    fraction_nitrified=0.25,
                    fraction_denitrified=0,
                    n2o_n=0.033,
                    no_n=0.0033,
                    n2_n=0.099,
                    n_leached=0.0575)

            # // Solid-stockpiled - beef
            # // Note 3
            case ManureStateType.deep_bedding | ManureStateType.solid_storage:
                return FractionOfOrganicNitrogenMineralizedData(
                    fraction_immobilized=0,
                    fraction_mineralized=0.28,
                    fraction_nitrified=0.125,
                    fraction_denitrified=0,
                    n2o_n=0.033,
                    no_n=0.0033,
                    n2_n=0.099,
                    n_leached=0.0575
                )
    elif animal_type.is_dairy_cattle_type():
        match state_type:
            # // Solid-compost - dairy
            # // Note 2
            case ManureStateType.compost_intensive | ManureStateType.compost_passive:
                return FractionOfOrganicNitrogenMineralizedData(
                    fraction_immobilized=0,
                    fraction_mineralized=0.46,
                    fraction_nitrified=0.282,
                    fraction_denitrified=0.152,
                    n2o_n=0.037,
                    no_n=0.0037,
                    n2_n=0.111,
                    n_leached=0.13)

            # // Solid-stockpiled - dairy
            # // Note 3
            case ManureStateType.deep_bedding | ManureStateType.solid_storage:
                return FractionOfOrganicNitrogenMineralizedData(
                    fraction_immobilized=0,
                    fraction_mineralized=0.28,
                    fraction_nitrified=0.141,
                    fraction_denitrified=0.076,
                    n2o_n=0.0185,
                    no_n=0.0019,
                    n2_n=0.0555,
                    n_leached=0.065)

    # // Liquid systems for both beef and dairy
    match state_type:
        # // Liquid with natural crust
        # // Note 5, 7
        case ManureStateType.liquid_with_natural_crust | ManureStateType.liquid_with_solid_cover | ManureStateType.deep_pit:
            return FractionOfOrganicNitrogenMineralizedData(
                fraction_immobilized=0,
                fraction_mineralized=0.1,
                fraction_nitrified=0.021 / min(1., fraction_of_tan_in_liquid_manure_storage_system),
                fraction_denitrified=0.021 / min(1., fraction_of_tan_in_liquid_manure_storage_system),
                n2o_n=0.005 / min(1., fraction_of_tan_in_liquid_manure_storage_system),
                no_n=0.0005 / min(1., fraction_of_tan_in_liquid_manure_storage_system),
                n2_n=0.015 / min(1., fraction_of_tan_in_liquid_manure_storage_system),
                n_leached=0)

        # // Liquid without natural crust
        # // Note 6, 7
        case ManureStateType.liquid_no_crust:
            return FractionOfOrganicNitrogenMineralizedData(
                fraction_immobilized=0,
                fraction_mineralized=0.1,
                fraction_nitrified=0.0,
                fraction_denitrified=0,
                n2o_n=0,
                no_n=0,
                n2_n=0,
                n_leached=0
            )

    return FractionOfOrganicNitrogenMineralizedData()
