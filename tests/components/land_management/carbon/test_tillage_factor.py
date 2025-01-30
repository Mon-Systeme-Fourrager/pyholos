import unittest

from numpy.random import choice

from holos_service.components.land_management.carbon import tillage_factor
from holos_service.components.land_management.common import TillageType
from holos_service.soil import SoilFunctionalCategory


class TestCalculateCropTillageFactor(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.considered_soil_functional_categories = []

    def test_existing_values(self):
        for soil_functional_category, tillage_type, expected_result in [
            (SoilFunctionalCategory.Brown, TillageType.Intensive, 1.0),
            (SoilFunctionalCategory.Brown, TillageType.Reduced, 0.9),
            (SoilFunctionalCategory.Brown, TillageType.NoTill, 0.8),
            (SoilFunctionalCategory.DarkBrown, TillageType.Intensive, 1.0),
            (SoilFunctionalCategory.DarkBrown, TillageType.Reduced, 0.85),
            (SoilFunctionalCategory.DarkBrown, TillageType.NoTill, 0.7),
            (SoilFunctionalCategory.Black, TillageType.Intensive, 1.0),
            (SoilFunctionalCategory.Black, TillageType.Reduced, 0.8),
            (SoilFunctionalCategory.Black, TillageType.NoTill, 0.6),
        ]:
            self.assertEqual(
                expected_result,
                tillage_factor.calculate_crop_tillage_factor(
                    soil_functional_category=soil_functional_category,
                    tillage_type=tillage_type))
            self.considered_soil_functional_categories.append(soil_functional_category)

    def test_values_from_outside_table(self):
        for soil_functional_category in SoilFunctionalCategory:
            if soil_functional_category not in [
                SoilFunctionalCategory.Brown,
                SoilFunctionalCategory.DarkBrown,
                SoilFunctionalCategory.Black
            ]:
                self.assertEqual(
                    1,
                    tillage_factor.calculate_crop_tillage_factor(
                        soil_functional_category=soil_functional_category,
                        tillage_type=choice(list(TillageType))
                    )
                )


if __name__ == '__main__':
    unittest.main()
