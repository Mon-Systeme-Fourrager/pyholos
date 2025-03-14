from dataclasses import dataclass
from datetime import date
from typing import Union, ClassVar

from pandas import DataFrame

from holos_service.components.animals.common import (ProductionStage, Diet, HousingType, ManureStateType,
                                                     DietAdditiveType, BeddingMaterialType, Milk,
                                                     get_manure_emission_factors)
from holos_service.django_stuff import CanadianProvince
from holos_service.soil import SoilTexture
from holos_service.utils import concat_lists

type ManagementPeriods = list[BeefManagementPeriod | DairyManagementPeriod]
from holos_service.components.animals import beef, dairy


class AnimalInputBase:
    def __init__(self):
        pass

    def __iter__(self):
        for k, v in self.__dict__.items():
            if v is not None:
                yield k, v

    def _filter_inputs(
            self,
            animal_groups: list[list[str]]
    ) -> list[list[str]]:
        res = []
        for component_type_animals in animal_groups:
            animal_data = [s for s in component_type_animals if getattr(self, s) is not None]
            if len(animal_data) > 0:
                res.append(animal_data)
        return res

    def filter_inputs(self) -> list[list[str]]:
        pass

    @staticmethod
    def map_component(**kwargs):
        pass

    @staticmethod
    def _create_component(**kwargs):
        pass

    def create_components(
            self,
            province: CanadianProvince,
            soil_texture: SoilTexture,
    ) -> list[DataFrame]:
        res = []
        for non_empty_entry in self.filter_inputs():
            animal_components = []
            for animal_type in non_empty_entry:
                management_periods = getattr(self, animal_type)
                component_type = self.map_component(component_name=animal_type)
                animal_components.append(
                    [self._create_component(
                        province=province,
                        soil_texture=soil_texture,
                        component_class=component_type,
                        management_period=management_period).to_dict()
                     for management_period in management_periods])

            res.append(DataFrame.from_records(concat_lists(*animal_components)))
        return res


@dataclass
class WeatherSummary:
    year: int
    mean_annual_precipitation: float
    mean_annual_temperature: float
    mean_annual_evapotranspiration: float
    growing_season_precipitation: float
    growing_season_evapotranspiration: float


@dataclass
class BeefManagementPeriod:
    name: str
    start_date: date
    days: int
    group_pairing_number: int
    number_of_animals: int
    production_stage: ProductionStage
    number_of_young_animals: int
    is_milk_fed_only: bool
    diet: Diet
    housing_type: HousingType
    manure_handling_system: ManureStateType
    weather_summary: WeatherSummary
    start_weight: float = None
    end_weight: float = None
    diet_additive_type: DietAdditiveType = DietAdditiveType.NONE
    bedding_material_type: BeddingMaterialType = BeddingMaterialType.straw


@dataclass
class DairyManagementPeriod:
    name: str
    start_date: date
    days: int
    group_pairing_number: int
    number_of_animals: int
    production_stage: ProductionStage
    number_of_young_animals: int
    milk_data: Milk()
    diet: Diet
    housing_type: HousingType
    manure_handling_system: ManureStateType
    weather_summary: WeatherSummary
    start_weight: float = None
    end_weight: float = None
    diet_additive_type: DietAdditiveType = DietAdditiveType.NONE
    bedding_material_type: BeddingMaterialType = BeddingMaterialType.straw


@dataclass
class BeefCattleInput(AnimalInputBase):
    Bulls: ManagementPeriods = None
    ReplacementHeifers: ManagementPeriods = None
    Cows: ManagementPeriods = None
    Calves: ManagementPeriods = None
    FinishingHeifers: ManagementPeriods = None
    FinishingSteers: ManagementPeriods = None
    BackgrounderHeifer: ManagementPeriods = None
    BackgrounderSteer: ManagementPeriods = None

    component_types: ClassVar = Union[
        beef.Bulls,
        beef.ReplacementHeifers,
        beef.Cows,
        beef.Calves,
        beef.FinishingHeifers,
        beef.FinishingSteers,
        beef.BackgrounderHeifer,
        beef.BackgrounderSteer]

    # def __post_init__(self):
    #     self.verify_is_one_animal_component_type()
    #
    # def get_animal_components(self) -> list[str]:
    #     return list(set([self.map_component(component_name=v).component_type.value for v, _ in self]))
    #
    # def verify_is_one_animal_component_type(self):
    #     animal_components = self.get_animal_components()
    #     assert len(animal_components) == 1, (
    #         f"All animal types must belong to the same component type (current components are {animal_components}).")

    def filter_inputs(self) -> list[list[str]]:
        return self._filter_inputs(animal_groups=[
            ["Bulls", "ReplacementHeifers", "Cows", "Calves"],
            ["FinishingHeifers", "FinishingSteers"],
            ["BackgrounderHeifer", "BackgrounderSteer"]
        ])

    @staticmethod
    def map_component(
            component_name: str
    ) -> component_types:

        match component_name:
            case 'Bulls':
                res = beef.Bulls
            case 'ReplacementHeifers':
                res = beef.ReplacementHeifers
            case 'Cows':
                res = beef.Cows
            case 'Calves':
                res = beef.Calves
            case 'FinishingHeifers':
                res = beef.FinishingHeifers
            case 'FinishingSteers':
                res = beef.FinishingSteers
            case 'BackgrounderHeifer':
                res = beef.BackgrounderHeifer
            case 'BackgrounderSteer':
                res = beef.BackgrounderSteer
            case _:
                raise ValueError(f'Unrecognized component name "({component_name})."')

        return res

    @staticmethod
    def _create_component(
            province: CanadianProvince,
            soil_texture: SoilTexture,
            component_class: [component_types],
            management_period: BeefManagementPeriod
    ) -> component_types:
        return component_class(
            management_period_name=management_period.name,
            management_period_start_date=management_period.start_date,
            management_period_days=management_period.days,
            group_pairing_number=management_period.group_pairing_number,
            production_stage=management_period.production_stage,
            number_of_animals=management_period.number_of_animals,
            number_of_young_animals=management_period.number_of_young_animals,
            is_milk_fed_only=management_period.is_milk_fed_only,
            milk_data=Milk(),
            diet=management_period.diet,
            housing_type=management_period.housing_type,
            manure_handling_system=management_period.manure_handling_system,
            manure_emission_factors=get_manure_emission_factors(
                animal_type=component_class.animal_type,
                year=management_period.weather_summary.year,
                manure_state_type=management_period.manure_handling_system,
                mean_annual_precipitation=management_period.weather_summary.mean_annual_precipitation,
                mean_annual_temperature=management_period.weather_summary.mean_annual_temperature,
                mean_annual_evapotranspiration=management_period.weather_summary.mean_annual_evapotranspiration,
                growing_season_precipitation=management_period.weather_summary.growing_season_precipitation,
                growing_season_evapotranspiration=management_period.weather_summary.growing_season_evapotranspiration,
                province=province,
                soil_texture=soil_texture),
            start_weight=management_period.start_weight,
            end_weight=management_period.end_weight,
            diet_additive_type=management_period.diet_additive_type,
            bedding_material_type=management_period.bedding_material_type
        )


@dataclass
class DairyCattleInput(AnimalInputBase):
    Heifers: ManagementPeriods = None
    LactatingCow: ManagementPeriods = None
    Calves: ManagementPeriods = None
    DryCow: ManagementPeriods = None

    component_types: ClassVar = Union[
        dairy.DairyHeifers,
        dairy.DairyLactatingCow,
        dairy.DairyCalves,
        dairy.DairyDryCow]

    @staticmethod
    def map_component(
            component_name: str
    ) -> component_types:

        match component_name:
            case 'Heifers':
                res = dairy.DairyHeifers
            case 'LactatingCow':
                res = dairy.DairyLactatingCow
            case 'Calves':
                res = dairy.DairyCalves
            case 'DryCow':
                res = dairy.DairyDryCow
            case _:
                raise ValueError(f'Unrecognized component name "({component_name})."')

        return res

    def filter_inputs(self) -> list[list[str]]:
        return self._filter_inputs(animal_groups=[
            ["Heifers", "LactatingCow", "Calves", "DryCow"]
        ])

    @staticmethod
    def _create_component(
            province: CanadianProvince,
            soil_texture: SoilTexture,
            component_class: [component_types],
            management_period: DairyManagementPeriod
    ) -> component_types:
        return component_class(
            management_period_name=management_period.name,
            management_period_start_date=management_period.start_date,
            management_period_days=management_period.days,
            group_pairing_number=management_period.group_pairing_number,
            number_of_animals=management_period.number_of_animals,
            production_stage=management_period.production_stage,
            number_of_young_animals=management_period.number_of_young_animals,
            milk_data=Milk(),
            diet=management_period.diet,
            housing_type=management_period.housing_type,
            manure_handling_system=management_period.manure_handling_system,
            diet_additive_type=management_period.diet_additive_type,
            bedding_material_type=management_period.bedding_material_type,

            manure_emission_factors=get_manure_emission_factors(
                manure_state_type=management_period.manure_handling_system,
                mean_annual_precipitation=management_period.weather_summary.mean_annual_precipitation,
                mean_annual_temperature=management_period.weather_summary.mean_annual_temperature,
                mean_annual_evapotranspiration=management_period.weather_summary.mean_annual_evapotranspiration,
                growing_season_precipitation=management_period.weather_summary.growing_season_precipitation,
                growing_season_evapotranspiration=management_period.weather_summary.growing_season_evapotranspiration,
                animal_type=component_class.animal_group.type,
                province=province,
                year=management_period.weather_summary.year,
                soil_texture=soil_texture)
        )


@dataclass
class SheepFlockInput:
    SheepFeedlot: ManagementPeriods = None
    Rams: ManagementPeriods = None
    Ewes: ManagementPeriods = None
    Lambs: ManagementPeriods = None
