import unittest

from holos_service.components.land_management import climate
from tests.helpers.utils import assert_is_ascending, assert_is_descending


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


class TestCalculateGreenAreaIndex(unittest.TestCase):
    def test_calculate_green_area_index_returns_green_area_index_max_at_mid_season(self):
        gai_max = 1
        self.assertEqual(
            gai_max,
            climate.calculate_green_area_index(
                green_area_index_max=gai_max,
                julian_day=100,
                mid_season=100,
                variance=1))

    def test_calculate_green_area_index_returns_increasing_values_towards_mid_season(self):
        mid_season = 100
        gai = [climate.calculate_green_area_index(
            green_area_index_max=1,
            julian_day=v,
            mid_season=mid_season,
            variance=1)
            for v in range(mid_season)
        ]

        assert_is_ascending(gai)

    def test_calculate_green_area_index_returns_decreasing_values_after_mid_season(self):
        mid_season = 100
        gai = [climate.calculate_green_area_index(
            green_area_index_max=1,
            julian_day=v,
            mid_season=mid_season,
            variance=1)
            for v in range(mid_season, mid_season + 100)
        ]

        assert_is_descending(gai)


class TestCalculateOrganicCarbonFactor(unittest.TestCase):
    def test_calculate_organic_carbon_factor_returns_expected_value_for_no_organic_carbon_in_soil(self):
        self.assertEqual(
            -0.837531,
            climate.calculate_organic_carbon_factor(percent_organic_carbon=0))

    def test_calculate_organic_carbon_factor_returns_zero_for_a_specific_value_of_organic_carbon_in_soil(self):
        self.assertEqual(
            0,
            climate.calculate_organic_carbon_factor(percent_organic_carbon=0.837531 / 0.430183))

    def test_calculate_organic_carbon_factor_returns_increasing_values_with_organic_carbon_in_soil(self):
        assert_is_ascending([climate.calculate_organic_carbon_factor(percent_organic_carbon=v)
                             for v in range(20)])


class TestCalculateClayFactor(unittest.TestCase):
    def test_calculate_clay_factor_returns_expected_value_for_zero_clay_content(self):
        self.assertEqual(
            -1.40744,
            climate.calculate_clay_factor(clay_content=0))

    def test_calculate_clay_factor_returns_zero_at_specific_value_of_clay_content(self):
        self.assertEqual(
            0,
            climate.calculate_clay_factor(clay_content=1.40744 / (0.0661969 * 100)))

    def test_calculate_clay_factor_returns_increasing_values_with_clay_content(self):
        assert_is_ascending([climate.calculate_clay_factor(clay_content=v) for v in range(100)])


class TestCalculateSandFactor(unittest.TestCase):
    def test_calculate_sand_factor_returns_expected_value_for_zero_sand_content(self):
        self.assertEqual(
            -1.51866,
            climate.calculate_sand_factor(sand_content=0))

    def test_calculate_sand_factor_returns_zero_at_specific_value_of_sand_content(self):
        self.assertEqual(
            0,
            climate.calculate_sand_factor(sand_content=1.51866 / (0.0393284 * 100)))

    def test_calculate_sand_factor_returns_increasing_values_with_sand_content(self):
        assert_is_ascending([climate.calculate_sand_factor(sand_content=v) for v in range(100)])


if __name__ == '__main__':
    unittest.main()
