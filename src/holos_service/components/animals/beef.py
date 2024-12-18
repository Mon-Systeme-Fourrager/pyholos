from pandas import DataFrame

from holos_service import utils
from holos_service.common import HolosVar, Component, EnumGeneric
from holos_service.components.animals.common import (
    HousingType,
    AnimalCoefficientData)
from holos_service.config import PathsHolosResources
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


class Beef(Component):
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
        self.methane_conversion_factor_adjusted = HolosVar(
            name="Methane Conversion Factor Adjusted",
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
        self.methane_conversion_factor_of_manure = HolosVar(
            name="Methane Conversion Factor Of Manure",
            value=None)
        self.n2o_direct_emission_factor = HolosVar(
            name="N2O Direct Emission Factor",
            value=None)
        self.emission_factor_volatilization = HolosVar(
            name="Emission Factor Volatilization",
            value=None)
        self.volatilization_fraction = HolosVar(
            name="Volatilization Fraction",
            value=None)
        self.emission_factor_leaching = HolosVar(
            name="Emission Factor Leaching",
            value=None)
        self.fraction_leaching = HolosVar(
            name="Fraction Leaching",
            value=None)
        self.ash_content = HolosVar(
            name="Ash Content",
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
