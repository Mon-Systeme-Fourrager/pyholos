import unittest

from holos_service.components.land_management import climate


class TestCalculateGreenAreaIndexMax(unittest.TestCase):
    def test_calculate_green_area_index_max_returns_zero_for_zero_yield(self):
        self.assertEqual(
            0,
            climate.calculate_green_area_index_max(crop_yield=0))

    def test_calculate_green_area_index_max_returns_expected_value_for_1000_kg_yield(self):
        self.assertEqual(
            0.0731 + 0.408,
            climate.calculate_green_area_index_max(crop_yield=1000))


class TestCalculateMidSeason(unittest.TestCase):
    def test_calculate_mid_season_returns_expected_results(self):
        for emergence_day, ripening_day in [
            (0, 100),
            (50, 150),
            (50, 50)
        ]:
            self.assertEqual(
                (emergence_day + ripening_day) / 2.,
                climate.calculate_mid_season(
                    emergence_day=emergence_day,
                    ripening_day=ripening_day))


if __name__ == '__main__':
    unittest.main()
