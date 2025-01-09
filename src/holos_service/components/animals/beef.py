from datetime import date

from pandas import DataFrame

from holos_service import utils
from holos_service.common import HolosVar, Component, EnumGeneric
from holos_service.components.animals.common import (
    ProductionStage, DietAdditiveType, Milk, Diet, HousingType,
    Bedding, AnimalType, BeddingMaterialType, AnimalCoefficientData,
    get_default_methane_producing_capacity_of_manure, ManureStateType,
    get_fraction_of_organic_nitrogen_mineralized_data,
    get_ammonia_emission_factor_for_storage_of_beef_and_dairy_cattle_manure, LivestockEmissionConversionFactorsData)
from holos_service.components.common import ComponentType
from holos_service.config import DATE_FMT, PathsHolosResources
from holos_service.django_stuff import CanadianProvince


def get_average_milk_production_for_dairy_cows_value(
        year: int,
        province: CanadianProvince
):
    """returns the average milk production value for a given Canadian Province.

    Args:
        year: year for which the average milk production will be returned
        province: Canadian Province object

    Returns:
        (kg head-1 day-1): the average milk production value

    References:
        Holos source code: https://github.com/holos-aafc/Holos/blob/396f1ab9bc7247e6d78766f9445c14d2eb7c0d9d/H.Core/Providers/Animals/Table_21_Average_Milk_Production_Dairy_Cows_Provider.cs#L56
    """
    df = utils.read_holos_resource_table(
        path_file=PathsHolosResources.Table_21_Average_Milk_Production_For_Dairy_Cows_By_Province,
        index_col='Year')
    year_min = min(df.index)
    year_max = max(df.index)

    df = df.merge(DataFrame(index=range(year_min, year_max + 1)), right_index=True, left_index=True, how="right")
    df.interpolate(method="linear", inplace=True)

    return df.loc[max(year_min, min(year_max, year)), province.value.abbreviation]


class GroupNames(EnumGeneric):
    bulls: str = "Bulls"
    replacement_heifers: str = "Replacement heifers"
    cows: str = "Cows"
    calves: str = "Calves"


class BeefBase(Component):
    def __init__(self):
        super().__init__()

        self.name = HolosVar(
            name="Name",
            value="Beef")
        self.component_type = HolosVar(
            name="Component Type",
            value="H.Core.Models.Animals.Beef")
        self.group_name = HolosVar(
            name="Group Name",
            value=None)
        self.group_type = HolosVar(
            name="Group Type",
            value=None)
        self.management_period_name = HolosVar(
            name="Management Period Name",
            value=None)
        self.group_pairing_number = HolosVar(
            name="Group Pairing Number",
            value=None)
        self.management_period_start_date = HolosVar(
            name="Management Period Start Date",
            value=None)
        self.management_period_days = HolosVar(
            name="Management Period Days",
            value=None)
        self.number_of_animals = HolosVar(
            name="Number Of Animals",
            value=None)
        self.production_stage = HolosVar(
            name="Production Stage",
            value=None)
        self.number_of_young_animals = HolosVar(
            name="Number Of Young Animals",
            value=None)
        self.animals_are_milk_fed_only = HolosVar(
            name="Animals Are Milk Fed Only",
            value=None)
        self.start_weight = HolosVar(
            name="Start Weight",
            value=None)
        self.end_weight = HolosVar(
            name="End Weight",
            value=None)
        self.average_daily_gain = HolosVar(
            name="Average Daily Gain",
            value=None)
        self.milk_production = HolosVar(
            name="Milk Production",
            value=None)
        self.milk_fat_content = HolosVar(
            name="Milk Fat Content",
            value=None)
        self.milk_protein_content_as_percentage = HolosVar(
            name="Milk Protein Content As Percentage",
            value=None)
        self.diet_additive_type = HolosVar(
            name="Diet Additive Type",
            value=None)
        self.methane_conversion_factor_of_diet = HolosVar(
            name="Methane Conversion Factor Of Diet",
            value=None)

        self.feed_intake = HolosVar(
            name="Feed Intake",
            value=None)
        self.crude_protein = HolosVar(
            name="Crude Protein",
            value=None)
        self.forage = HolosVar(
            name="Forage",
            value=None)
        self.tdn = HolosVar(
            name="TDN",
            value=None)
        self.ash_content_of_diet = HolosVar(
            name="Ash Content Of Diet",
            value=None)
        self.starch = HolosVar(
            name="Starch",
            value=None)
        self.fat = HolosVar(
            name="Fat",
            value=None)
        self.me = HolosVar(
            name="ME",
            value=None)
        self.ndf = HolosVar(
            name="NDF",
            value=None)
        self.dietary_net_energy_concentration = HolosVar(
            name="Dietary Net Energy Concentration",
            value=None)
        self.housing_type = HolosVar(
            name="Housing Type",
            value=None)
        self.gain_coefficient = HolosVar(
            name="Gain Coefficient",
            value=None)
        self.user_defined_bedding_rate = HolosVar(
            name="User Defined Bedding Rate",
            value=None)
        self.total_carbon_kilograms_dry_matter_for_bedding = HolosVar(
            name="Total Carbon Kilograms Dry Matter For Bedding",
            value=None)
        self.total_nitrogen_kilograms_dry_matter_for_bedding = HolosVar(
            name="Total Nitrogen Kilograms Dry Matter For Bedding",
            value=None)
        self.moisture_content_of_bedding_material = HolosVar(
            name="Moisture Content Of Bedding Material",
            value=None)
        self.activity_coefficient_of_feeding_situation = HolosVar(
            name="Activity Coefficient Of Feeding Situation",
            value=None)

        self.maintenance_coefficient = HolosVar(
            name="Maintenance Coefficient",
            value=None)
        """(MJ day⁻¹ kg⁻¹) C_f_adjusted"""

        self.methane_conversion_factor_of_manure = HolosVar(
            name="Methane Conversion Factor Of Manure",
            value=None)
        self.n2o_direct_emission_factor = HolosVar(
            name="N2O Direct Emission Factor",
            value=None)

        self.emission_factor_volatilization = HolosVar(
            name="Emission Factor Volatilization",
            value=None)
        """(kg N2O-N (kg N)^-1) EF_volatilization
        """

        self.volatilization_fraction = HolosVar(
            name="Volatilization Fraction",
            value=None)
        self.emission_factor_leaching = HolosVar(
            name="Emission Factor Leaching",
            value=None)
        self.fraction_leaching = HolosVar(
            name="Fraction Leaching",
            value=None)

        self.methane_producing_capacity_of_manure = HolosVar(
            name="Methane Producing Capacity Of Manure",
            value=None)
        self.fraction_of_organic_nitrogen_immobilized = HolosVar(
            name="Fraction Of Organic Nitrogen Immobilized",
            value=None)
        self.fraction_of_organic_nitrogen_nitrified = HolosVar(
            name="Fraction Of Organic Nitrogen Nitrified",
            value=None)
        self.fraction_of_organic_nitrogen_mineralized = HolosVar(
            name="Fraction Of Organic Nitrogen Mineralized",
            value=None)
        self.manure_state_type = HolosVar(
            name="Manure State Type",
            value=None)
        self.ammonia_emission_factor_for_manure_storage = HolosVar(
            name="Ammonia Emission Factor For Manure Storage",
            value=None)

        self.methane_conversion_factor_adjusted = HolosVar(
            name="Methane Conversion Factor Adjusted",
            value=0)
        """deprecated"""

        self.ash_content = HolosVar(
            name="Ash Content",
            value=8.0)
        """deprecated"""

        self._animal_coefficient_data: AnimalCoefficientData | None = None

    def get_animal_coefficient_data(self):
        df = utils.read_holos_resource_table(
            path_file=PathsHolosResources.Table_16_Livestock_Coefficients_BeefAndDairy_Cattle_Provider,
            index_col="AnimalType")

        if self.group_type.value in df.index:
            _df = df.loc[self.group_type.value]
            self._animal_coefficient_data = AnimalCoefficientData(
                baseline_maintenance_coefficient=_df['BaselineMaintenanceCoefficient'],
                gain_coefficient=_df['GainCoefficient'],
                default_initial_weight=_df['DefaultInitialWeight'],
                default_final_weight=_df['DefaultFinalWeight'])
        else:
            self._animal_coefficient_data = AnimalCoefficientData()
        pass

    def update_name(self, name: str):
        self.name.value = ' '.join((self.name.value, name))

    def update_component_type(self, component_type: str):
        self.component_type.value = '.'.join((self.component_type.value, component_type))

    def get_feeding_activity_coefficient(self):
        match self.housing_type.value:
            case HousingType.housed_in_barn | HousingType.confined | HousingType.confined_no_barn:
                res = 0

            case HousingType.pasture | HousingType.flat_pasture | HousingType.enclosed_pasture:
                res = 0.17

            case HousingType.open_range_or_hills:
                res = 0.36

            case _:
                res = 0

        self.activity_coefficient_of_feeding_situation.value = res
        pass


class Beef(BeefBase):
    def __init__(
            self,
            name: str,
            component_type: ComponentType,
            group_name: GroupNames,
            animal_type: AnimalType,
            management_period_name: str,
            group_pairing_number: int,
            management_period_start_date: date,
            management_period_days: int,
            number_of_animals: int,
            production_stage: ProductionStage,
            number_of_young_animals: int,
            is_milk_fed_only: bool,
            milk_data: Milk,
            diet: Diet,
            housing_type: HousingType,
            manure_handling_system: ManureStateType,
            manure_emission_factors: LivestockEmissionConversionFactorsData,
            start_weight: float = None,
            end_weight: float = None,
            diet_additive_type: DietAdditiveType = DietAdditiveType.NONE,
            bedding_material_type: BeddingMaterialType = BeddingMaterialType.NONE,
    ):
        """

        Args:
            group_name: GroupNames member
            animal_type: AnimalType class instance
            management_period_name: given name for the management period
            group_pairing_number: number of paired animals
            management_period_start_date: starting date for the management period
            management_period_days: number of days of the management period
            number_of_animals: number of animals
            production_stage: ProductionStage class instance
            number_of_young_animals: number of young animals
            is_milk_fed_only: used to indicate when animals are not consuming forage but only milk (distinction needed for calculate enteric methane for beef calves)
            start_weight: (kg) animal weight at the beginning of the management period
            end_weight: (kg) animal weight at the end of the management period
            milk_data: class object that contains all required milk production data
            diet: class object that contains all required diet data
            diet_additive_type: type of the diet additive
            bedding_material_type: bedding material type
        """
        super().__init__()
        self.update_name(name=name)
        self.update_component_type(component_type.to_str())

        self.group_name.value = group_name.value
        self.group_type.value = animal_type.value
        self.management_period_name.value = management_period_name
        self.group_pairing_number.value = group_pairing_number
        self.management_period_start_date.value = management_period_start_date.strftime(DATE_FMT)
        self.management_period_days.value = management_period_days
        self.number_of_animals.value = number_of_animals
        self.production_stage.value = production_stage.value
        self.number_of_young_animals.value = number_of_young_animals
        self.animals_are_milk_fed_only.value = str(is_milk_fed_only).upper()

        self.get_animal_coefficient_data()
        self.maintenance_coefficient.value = self._animal_coefficient_data.baseline_maintenance_coefficient
        self.gain_coefficient.value = self._animal_coefficient_data.gain_coefficient

        self.start_weight.value = self._animal_coefficient_data.default_initial_weight if start_weight is None else start_weight
        self.end_weight.value = self._animal_coefficient_data.default_final_weight if end_weight is None else end_weight

        self.average_daily_gain.value = (self.end_weight.value - self.start_weight.value) / management_period_days
        self.milk_production.value = milk_data.production
        self.milk_fat_content.value = milk_data.fat_content
        self.milk_protein_content_as_percentage.value = milk_data.protein_content_as_percentage

        self.diet_additive_type.value = diet_additive_type.value
        # self.methane_conversion_factor_adjusted.value = 0
        self.feed_intake.value = 0

        self.crude_protein.value = diet.crude_protein_percentage
        self.forage.value = diet.forage_percentage
        self.tdn.value = diet.total_digestible_nutrient_percentage
        self.ash_content_of_diet.value = diet.ash_percentage
        self.starch.value = diet.starch_percentage
        self.fat.value = diet.fat_percentage
        self.me.value = diet.metabolizable_energy
        self.ndf.value = diet.neutral_detergent_fiber_percentage

        self.dietary_net_energy_concentration.value = diet.calc_dietary_net_energy_concentration_for_beef()
        self.methane_conversion_factor_of_diet.value = diet.calc_methane_conversion_factor(animal_type=animal_type)

        self.housing_type.value = housing_type.value

        bedding = Bedding(
            housing_type=housing_type,
            bedding_material_type=bedding_material_type,
            animal_type=animal_type)

        self.user_defined_bedding_rate.value = bedding.user_defined_bedding_rate.value
        self.total_carbon_kilograms_dry_matter_for_bedding.value = bedding.total_carbon_kilograms_dry_matter_for_bedding.value
        self.total_nitrogen_kilograms_dry_matter_for_bedding.value = bedding.total_nitrogen_kilograms_dry_matter_for_bedding.value
        self.moisture_content_of_bedding_material.value = bedding.moisture_content_of_bedding_material.value

        self.get_feeding_activity_coefficient()

        self.methane_producing_capacity_of_manure.value = get_default_methane_producing_capacity_of_manure(
            is_pasture=housing_type.is_pasture(),
            animal_type=animal_type)

        fraction_of_organic_nitrogen_mineralized_data = get_fraction_of_organic_nitrogen_mineralized_data(
            state_type=manure_handling_system,
            animal_type=animal_type)

        self.manure_state_type.value = manure_handling_system.value
        self.fraction_of_organic_nitrogen_immobilized.value = fraction_of_organic_nitrogen_mineralized_data.fraction_immobilized
        self.fraction_of_organic_nitrogen_nitrified.value = fraction_of_organic_nitrogen_mineralized_data.fraction_nitrified
        self.fraction_of_organic_nitrogen_mineralized.value = fraction_of_organic_nitrogen_mineralized_data.fraction_mineralized

        self.ammonia_emission_factor_for_manure_storage.value = (
            get_ammonia_emission_factor_for_storage_of_beef_and_dairy_cattle_manure(
                storage_type=manure_handling_system))

        self.methane_conversion_factor_of_manure.value = manure_emission_factors.MethaneConversionFactor
        self.n2o_direct_emission_factor.value = manure_emission_factors.N2ODirectEmissionFactor
        self.volatilization_fraction.value = manure_emission_factors.VolatilizationFraction
        self.emission_factor_volatilization.value = manure_emission_factors.EmissionFactorVolatilization
        self.fraction_leaching.value = manure_emission_factors.LeachingFraction
        self.emission_factor_leaching.value = manure_emission_factors.EmissionFactorLeach


class Bulls(Beef):
    def __init__(
            self,
            management_period_name: str,
            group_pairing_number: int,
            management_period_start_date: date,
            management_period_days: int,
            number_of_animals: int,
            production_stage: ProductionStage,
            number_of_young_animals: int,
            is_milk_fed_only: bool,
            milk_data: Milk,
            diet: Diet,
            housing_type: HousingType,
            manure_handling_system: ManureStateType,
            manure_emission_factors: LivestockEmissionConversionFactorsData,
            start_weight: float = None,
            end_weight: float = None,
            diet_additive_type: DietAdditiveType = DietAdditiveType.NONE,
            bedding_material_type: BeddingMaterialType = BeddingMaterialType.NONE,
    ):
        """

        Args:
            management_period_name: given name for the management period
            group_pairing_number: number of paired animals
            management_period_start_date: starting date for the management period
            management_period_days: number of days of the management period
            number_of_animals: number of animals
            production_stage: ProductionStage class instance
            number_of_young_animals: number of young animals
            is_milk_fed_only: used to indicate when animals are not consuming forage but only milk (distinction needed for calculate enteric methane for beef calves)
            start_weight: (kg) animal weight at the beginning of the management period
            end_weight: (kg) animal weight at the end of the management period
            milk_data: class object that contains all required milk production data
            diet: class object that contains all required diet data
            diet_additive_type: type of the diet additive
            bedding_material_type: bedding material type
        """
        super().__init__(
            name='Cow-Calf',
            component_type=ComponentType.cow_calf,
            group_name=GroupNames.bulls,
            animal_type=AnimalType.beef_bulls,

        **utils.get_local_args(locals())
        )
