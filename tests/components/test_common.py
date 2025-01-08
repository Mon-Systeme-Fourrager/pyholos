import unittest

from holos_service.components import common


class TestComponentType(unittest.TestCase):
    def test_to_str(self):
        for component_type in common.ComponentType:
            self.assertEqual(
                component_type.value,
                component_type.to_str().replace('Component', '')
            )


class TestCalculateFractionOfNitrogenLostByLeachingAndRunoff(unittest.TestCase):
    def test_value_when_precipitation_is_lower_than_evapotranspiration(self):
        self.assertEqual(
            0.13765,
            common.calculate_fraction_of_nitrogen_lost_by_leaching_and_runoff(
                growing_season_precipitation=1,
                growing_season_evapotranspiration=2))

    def test_value_when_precipitation_is_higher_than_evapotranspiration(self):
        self.assertEqual(
            0.3,
            common.calculate_fraction_of_nitrogen_lost_by_leaching_and_runoff(
                growing_season_precipitation=2,
                growing_season_evapotranspiration=1))

    def test_max_value(self):
        evapotranspiration = 1
        for precipitation_to_evapotranspiration_ratio in range(1, 11):
            self.assertEqual(
                0.3,
                common.calculate_fraction_of_nitrogen_lost_by_leaching_and_runoff(
                    growing_season_precipitation=precipitation_to_evapotranspiration_ratio * evapotranspiration,
                    growing_season_evapotranspiration=evapotranspiration))

    def test_min_value(self):
        evapotranspiration = 1
        for evapotranspiration_to_precipitation_ratio in range(5, 11):
            self.assertEqual(
                0.05,
                common.calculate_fraction_of_nitrogen_lost_by_leaching_and_runoff(
                    growing_season_precipitation=evapotranspiration / evapotranspiration_to_precipitation_ratio,
                    growing_season_evapotranspiration=evapotranspiration))


if __name__ == '__main__':
    unittest.main()
