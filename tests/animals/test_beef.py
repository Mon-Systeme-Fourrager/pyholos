import unittest

from holos_service.components.animals import beef, common
from holos_service.core_constants import CoreConstants


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

    def run_gain_coefficient_test(
            self,
            animal_type: common.AnimalType,
            expected_value: float
    ) -> None:
        self.beef.group_type.value = animal_type.value
        self.beef.get_gain_coefficient()
        self.assertEqual(
            expected_value,
            self.beef.gain_coefficient.value)

    def test_get_gain_coefficient_returns_expected(self):
        animal_types = list(common.AnimalType)
        for animal_type, expected_value in [
            (common.AnimalType.beef_calf, CoreConstants.NotApplicable),
            (common.AnimalType.beef_cow_lactating, 0.8),
            (common.AnimalType.beef_cow_dry, 0.8),
            (common.AnimalType.beef_bulls, 1.2),
            (common.AnimalType.beef_backgrounder_steer, 1),
            (common.AnimalType.beef_backgrounder_heifer, 0.8),
            (common.AnimalType.beef_replacement_heifers, 0.8),
            (common.AnimalType.beef_finishing_steer, 1),
            (common.AnimalType.beef_finishing_heifer, 0.8),
            (common.AnimalType.dairy_lactating_cow, 0.8),
            (common.AnimalType.dairy_dry_cow, 0.8),
            (common.AnimalType.dairy_heifers, 0.8),
            (common.AnimalType.dairy_bulls, 1.2),
            (common.AnimalType.dairy_calves, 0),
        ]:
            self.run_gain_coefficient_test(animal_type=animal_type, expected_value=expected_value)
            animal_types.pop(animal_types.index(animal_type))

        for animal_type in animal_types:
            print(animal_type)
            self.run_gain_coefficient_test(animal_type=animal_type, expected_value=0)

    def test_update_name(self):
        old_name = self.beef.name.value
        new_name = 'test_name'
        self.beef.update_name(name=new_name)
        self.assertEqual(
            ' '.join((old_name, new_name)),
            self.beef.name.value)

if __name__ == '__main__':
    unittest.main()
