import unittest
from random import choice

from holos_service.components.land_management.carbon import tillage_factor
from holos_service.components.land_management.common import TillageType
from holos_service.django_stuff import CanadianProvince
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


class TestCalculateTillageFactorForPerennials(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.prairie_provinces = [
            CanadianProvince.Alberta,
            CanadianProvince.Saskatchewan,
            CanadianProvince.Manitoba]

    def test_value_for_prairie_provinces(self):
        for province in self.prairie_provinces:
            for soil_functional_category, expected_value in [
                (SoilFunctionalCategory.Brown, 0.8),
                (SoilFunctionalCategory.DarkBrown, 0.7),
                (SoilFunctionalCategory.Black, 0.6),
            ]:
                self.assertEqual(
                    expected_value,
                    tillage_factor.calculate_tillage_factor_for_perennials(
                        soil_functional_category=soil_functional_category,
                        province=province))

    def test_value_for_non_prairie_provinces(self):
        for province in CanadianProvince:
            if province not in self.prairie_provinces:
                self.assertEqual(
                    0.9,
                    tillage_factor.calculate_tillage_factor_for_perennials(
                        soil_functional_category=choice(list(SoilFunctionalCategory)),
                        province=province))


if __name__ == '__main__':
    unittest.main()
