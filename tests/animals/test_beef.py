import unittest

from holos_service.components.animals import beef, common


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


if __name__ == '__main__':
    unittest.main()
