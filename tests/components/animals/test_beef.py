import unittest

from holos_service.components.animals import beef, common
from holos_service.config import PathsHolosResources
from holos_service.core_constants import CoreConstants
from holos_service.django_stuff import CanadianProvince
from holos_service.utils import read_holos_resource_table


class TestBeef(unittest.TestCase):
    def setUp(self):
        self.beef = beef.Beef()

    def run_feeding_activity_test(
            self,
            housing_type: common.HousingType,
            expected_value: float
    ) -> None:
        self.beef.housing_type.value = housing_type
        self.beef.get_feeding_activity_coefficient()
        self.assertEqual(
            expected_value,
            self.beef.activity_coefficient_of_feeding_situation.value)

    def test_get_feeding_activity_coefficient_returns_expected_values(self):
        housing_types = list(common.HousingType)

        for housing_type, expected_value in [
            (common.HousingType.housed_in_barn, 0),
            (common.HousingType.confined, 0),
            (common.HousingType.confined_no_barn, 0),
            (common.HousingType.pasture, 0.17),
            (common.HousingType.flat_pasture, 0.17),
            (common.HousingType.enclosed_pasture, 0.17),
            (common.HousingType.open_range_or_hills, 0.36)
        ]:
            self.run_feeding_activity_test(housing_type=housing_type, expected_value=expected_value)

            housing_types.pop(housing_types.index(housing_type))

        for housing_type in housing_types:
            self.run_feeding_activity_test(housing_type=housing_type, expected_value=0)

    def run_animal_coefficient_data_test(
            self,
            animal_type: common.AnimalType,
            expected_baseline_maintenance_coefficient: float,
            expected_gain_coefficient: float,
            expected_default_initial_weight: float,
            expected_default_final_weight: float
    ) -> None:
        self.beef.group_type.value = animal_type.value
        self.beef.get_animal_coefficient_data()

        self.assertEqual(
            expected_baseline_maintenance_coefficient,
            self.beef._animal_coefficient_data.baseline_maintenance_coefficient)

        self.assertEqual(
            expected_gain_coefficient,
            self.beef._animal_coefficient_data.gain_coefficient)

        self.assertEqual(
            expected_default_initial_weight,
            self.beef._animal_coefficient_data.default_initial_weight)

        self.assertEqual(
            expected_default_final_weight,
            self.beef._animal_coefficient_data.default_final_weight)

    def test_animal_coefficient_data_returns_expected(self):
        animal_types = list(common.AnimalType)
        for animal_type, (baseline_maintenance_coefficient,
                          gain_coefficient,
                          default_initial_weight,
                          default_final_weight) in [
            (common.AnimalType.beef_calf, (CoreConstants.NotApplicable, CoreConstants.NotApplicable, 39, 260)),
            (common.AnimalType.beef_cow_lactating, (0.386, 0.8, 610, 610)),
            (common.AnimalType.beef_cow_dry, (0.322, 0.8, 610, 610)),
            (common.AnimalType.beef_bulls, (0.37, 1.2, 900, 900)),
            (common.AnimalType.beef_backgrounder_steer, (0.322, 1.0, 250, 380)),
            (common.AnimalType.beef_backgrounder_heifer, (0.322, 0.8, 240, 360)),
            (common.AnimalType.beef_replacement_heifers, (0.322, 0.8, 240, 360)),
            (common.AnimalType.beef_finishing_steer, (0.322, 1.0, 310, 610)),
            (common.AnimalType.beef_finishing_heifer, (0.322, 0.8, 300, 580)),
            (common.AnimalType.dairy_lactating_cow, (0.386, 0.8, 687, 687)),
            (common.AnimalType.dairy_dry_cow, (0.322, 0.8, 687, 687)),
            (common.AnimalType.dairy_heifers, (0.322, 0.8, 637, 687)),
            (common.AnimalType.dairy_bulls, (0.37, 1.2, 1200, 1200)),
            (common.AnimalType.dairy_calves, (0.0, 0.0, 45, 127)),
        ]:
            self.run_animal_coefficient_data_test(
                animal_type=animal_type,
                expected_baseline_maintenance_coefficient=baseline_maintenance_coefficient,
                expected_gain_coefficient=gain_coefficient,
                expected_default_initial_weight=default_initial_weight,
                expected_default_final_weight=default_final_weight)

            animal_types.pop(animal_types.index(animal_type))

        for animal_type in animal_types:
            print(animal_type)
            self.run_animal_coefficient_data_test(
                animal_type=animal_type,
                expected_baseline_maintenance_coefficient=0,
                expected_gain_coefficient=0,
                expected_default_initial_weight=0,
                expected_default_final_weight=0)

    def test_update_name(self):
        old_name = self.beef.name.value
        new_name = 'test_name'
        self.beef.update_name(name=new_name)
        self.assertEqual(
            ' '.join((old_name, new_name)),
            self.beef.name.value)

    def test_update_component_type(self):
        old_name = self.beef.component_type.value
        new_name = 'test_name'
        self.beef.update_component_type(component_type=new_name)
        self.assertEqual(
            '.'.join((old_name, new_name)),
            self.beef.component_type.value)


class TestGetAverageMilkProductionForDairyCowsValue(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.table_21 = read_holos_resource_table(
            path_file=PathsHolosResources.Table_21_Average_Milk_Production_For_Dairy_Cows_By_Province,
            index_col='Year')

        cls.provinces = [v for v in CanadianProvince if not v in (
            CanadianProvince.NorthwestTerritories,
            CanadianProvince.Nunavut,
            CanadianProvince.Yukon)]

    def test_original_table_expected_values_returned(self):
        for province in self.provinces:
            for year in self.table_21.index:
                self.assertEqual(
                    self.table_21.loc[year, province.value.abbreviation],
                    beef.get_average_milk_production_for_dairy_cows_value(
                        province=province,
                        year=year))

    def test_interpolated_values_returned(self):
        years = range(self.table_21.index.min(), self.table_21.index.max() + 1)
        for province in self.provinces:
            for year in years:
                if year not in self.table_21.index:
                    self.assertIsNotNone(
                        beef.get_average_milk_production_for_dairy_cows_value(
                            province=province,
                            year=year))

    def test_values_returned_for_oldest_year_for_years_older_than_oldest_year(self):
        year = self.table_21.index.min()
        for province in self.provinces:
            self.assertEqual(
                self.table_21.loc[year, province.value.abbreviation],
                beef.get_average_milk_production_for_dairy_cows_value(
                    province=province,
                    year=year - 1))

    def test_values_returned_for_most_recent_year_for_years_later_than_the_most_recent_year(self):
        year = self.table_21.index.max()
        for province in self.provinces:
            self.assertEqual(
                self.table_21.loc[year, province.value.abbreviation],
                beef.get_average_milk_production_for_dairy_cows_value(
                    province=province,
                    year=year + 1))


if __name__ == '__main__':
    unittest.main()
