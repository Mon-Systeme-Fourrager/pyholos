from enum import Enum

from holos_service import utils
from holos_service.common import Component, HolosVar
from holos_service.components.animals.common import AnimalType, convert_animal_type_name
from holos_service.config import PathsHolosResources


class GroupNames(Enum):
    sheep_feedlot: str = "Sheep feedlot"
    rams: str = "Rams"
    ewes: str = "Ewes"
    lambs: str = "Lambs"


class AnimalCoefficientData:
    def __init__(
            self,
            maintenance_coefficient: float = 0,
            coefficient_a: float = 0,
            coefficient_b: float = 0,
            initial_weight: float = 0,
            final_weight: float = 0,
            wool_production: float = 0
    ):
        """Table_22_Livestock_Coefficients_For_Sheep.csv

        Args:
            maintenance_coefficient: (MJ d-1 kg-1) maintenance coefficient (cf)
            coefficient_a: (MJ kg-1)
            coefficient_b: (MJ kg-2)
            initial_weight: (kg)
            final_weight: (kg)
            wool_production: : (kg year-1)
        """
        self.cf = maintenance_coefficient
        self.coefficient_a = coefficient_a
        self.coefficient_b = coefficient_b
        self.initial_weight = initial_weight
        self.final_weight = final_weight
        self.wool_production = wool_production


class Sheep(Component):
    def __init__(self):
        super().__init__()

        self.name = HolosVar(name="Name", value="Sheep")
        self.component_type = HolosVar(name="Component Type", value="H.Core.Models.Animals.Sheep")
        self.group_name = HolosVar(name="Group Name", value=None)
        self.group_type = HolosVar(name="Group Type", value=None)
        self.management_period_name = HolosVar(name="Management Period Name", value=None)
        self.group_pairing_number = HolosVar(name="Group Pairing Number", value=None)
        self.management_period_start_date = HolosVar(name="Management Period Start Date", value=None)
        self.management_period_days = HolosVar(name="Management Period Days", value=None)
        self.number_of_animals = HolosVar(name="Number Of Animals", value=None)
        self.production_stage = HolosVar(name="Production Stage", value=None)
        self.number_of_young_animals = HolosVar(name="Number Of Young Animals", value=None)
        self.start_weight = HolosVar(name="Start Weight", value=None)
        self.end_weight = HolosVar(name="End Weight", value=None)
        self.average_daily_gain = HolosVar(name="Average Daily Gain", value=None)
        self.energy_required_to_produce_wool = HolosVar(name="Energy Required To Produce Wool", value=None)
        self.wool_production = HolosVar(name="Wool Production", value=None)
        self.energy_required_to_produce_milk = HolosVar(name="Energy Required To Produce Milk", value=None)
        self.diet_additive_type = HolosVar(name="Diet Additive Type", value=None)
        self.feed_intake = HolosVar(name="Feed Intake", value=None)
        self.crude_protein = HolosVar(name="Crude Protein", value=None)
        self.forage = HolosVar(name="Forage", value=None)
        self.tdn = HolosVar(name="TDN", value=None)
        self.ash_content_of_diet = HolosVar(name="Ash Content Of Diet", value=None)
        self.starch = HolosVar(name="Starch", value=None)
        self.fat = HolosVar(name="Fat", value=None)
        self.me = HolosVar(name="ME", value=None)
        self.ndf = HolosVar(name="NDF", value=None)
        self.gain_coefficient_a = HolosVar(name="Gain Coefficient A", value=None)
        self.gain_coefficient_b = HolosVar(name="Gain Coefficient B", value=None)
        self.activity_coefficient_of_feeding_situation = HolosVar(name="Activity Coefficient Of Feeding Situation",
                                                                  value=None)
        self.maintenance_coefficient = HolosVar(name="Maintenance Coefficient", value=None)
        self.user_defined_bedding_rate = HolosVar(name="User Defined Bedding Rate", value=None)
        self.total_carbon_kilograms_dry_matter_for_bedding = HolosVar(
            name="Total Carbon Kilograms Dry Matter For Bedding", value=None)
        self.total_nitrogen_kilograms_dry_matter_for_bedding = HolosVar(
            name="Total Nitrogen Kilograms Dry Matter For Bedding", value=None)
        self.moisture_content_of_bedding_material = HolosVar(name="Moisture Content Of Bedding Material", value=None)
        self.methane_conversion_factor_of_manure = HolosVar(name="Methane Conversion Factor Of Manure", value=None)
        self.n2o_direct_emission_factor = HolosVar(name="N2O Direct Emission Factor", value=None)
        self.emission_factor_volatilization = HolosVar(name="Emission Factor Volatilization", value=None)
        self.volatilization_fraction = HolosVar(name="Volatilization Fraction", value=None)
        self.emission_factor_leaching = HolosVar(name="Emission Factor Leaching", value=None)
        self.fraction_leaching = HolosVar(name="Fraction Leaching", value=None)
        self.methane_conversion_factor_of_diet = HolosVar(name="Methane Conversion Factor Of Diet", value=None)
        self.methane_producing_capacity_of_manure = HolosVar(name="Methane Producing Capacity Of Manure", value=None)
        self.manure_excretion_rate = HolosVar(name="Manure Excretion Rate", value=None)
        self.fraction_of_carbon_in_manure = HolosVar(name="Fraction Of Carbon In Manure", value=None)

        self.methane_conversion_factor_adjusted = HolosVar(name="Methane Conversion Factor Adjusted", value=0)
        """deprecated"""

        self.ash_content = HolosVar(name="Ash Content", value=8.0)
        """deprecated"""

    def update_component_type(self, component_type: str):
        self.component_type.value = '.'.join((self.component_type.value, component_type))

    def update_group_type(self, group_name: str):
        self.group_type.value = group_name.title().replace(' ', '')

    def get_animal_coefficient_data(self) -> AnimalCoefficientData:
        df = utils.read_holos_resource_table(
            path_file=PathsHolosResources.Table_22_Livestock_Coefficients_For_Sheep)
        df.set_index(df.pop("Sheep Class").apply(lambda x: convert_animal_type_name(name=x)), inplace=True)

        animal_type = convert_animal_type_name(name=self.group_name.value)
        lookup_type = AnimalType.ram if animal_type == AnimalType.sheep_feedlot else animal_type

        if lookup_type in df.index:
            _df = df.loc[lookup_type]
            res = AnimalCoefficientData(
                maintenance_coefficient=_df['cf'],
                coefficient_a=_df['a'],
                coefficient_b=_df['b'],
                initial_weight=_df['Initial Weight'],
                final_weight=_df['Final Weight'],
                wool_production=_df['Wool Production'])
        else:
            res = AnimalCoefficientData()
        return res
