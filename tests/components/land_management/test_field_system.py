import unittest
from itertools import product

from holos_service.components.land_management import field_system
from holos_service.components.land_management.common import HarvestMethod, IrrigationType
from holos_service.components.land_management.crop import CropType
from holos_service.defaults import Defaults
from tests.helpers.utils import CropTypePerCategory


class TestLandManagementBase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.silage_crops = [
            CropType.SilageCorn,
            CropType.GrassSilage,
            CropType.BarleySilage,
            CropType.OatSilage,
            CropType.TriticaleSilage,
            CropType.WheatSilage
        ]

    def setUp(self):
        self.land_management_base = field_system.LandManagementBase()

    def test_get_default_harvest_method_for_silage_crops(self):
        for crop_type in CropTypePerCategory.silage_crop:
            self.land_management_base.crop_type.value = crop_type
            self.assertEqual(
                HarvestMethod.Silage,
                self.land_management_base.get_default_harvest_method())

    def test_get_default_harvest_method_for_non_silage_crops(self):
        for crop_type in CropType:
            if crop_type not in CropTypePerCategory.silage_crop:
                self.land_management_base.crop_type.value = crop_type
                self.assertEqual(
                    HarvestMethod.CashCrop,
                    self.land_management_base.get_default_harvest_method())

    def test_set_irrigation_type(self):
        for irrigation_amount, expected_result in [
            (0, IrrigationType.RainFed),
            (100, IrrigationType.Irrigated),
        ]:
            self.land_management_base.amount_of_irrigation.value = irrigation_amount
            self.land_management_base.set_irrigation_type()
            self.assertEqual(
                expected_result,
                self.land_management_base.irrigation_type.value)

    def test_set_moisture_content_fresh_crop_harvest(self):
        for crop, harvest_method in product(CropTypePerCategory.silage_crop, [
            HarvestMethod.GreenManure,
            HarvestMethod.Silage,
            HarvestMethod.Swathing
        ]):
            self.land_management_base.crop_type.value = crop
            self.land_management_base.harvest_method.value = harvest_method
            self.land_management_base.set_moisture_content()
            self.assertEqual(
                65,
                self.land_management_base.moisture_content_of_crop_percentage.value)

    def test_set_moisture_content_default_non_fresh_crop_harvest_methods(self):
        self.land_management_base.moisture_content_of_crop.value = 15

        for crop in CropType:
            if crop not in CropTypePerCategory.silage_crop:
                for harvest_method in HarvestMethod:
                    if harvest_method not in [
                        HarvestMethod.GreenManure,
                        HarvestMethod.Silage,
                        HarvestMethod.Swathing
                    ]:
                        self.land_management_base.crop_type.value = crop
                        self.land_management_base.harvest_method.value = harvest_method
                        self.land_management_base.set_moisture_content()
                        self.assertEqual(
                            self.land_management_base.moisture_content_of_crop.value,
                            self.land_management_base.moisture_content_of_crop_percentage.value)

    def test_set_moisture_content_default_value(self):
        self.land_management_base.moisture_content_of_crop.value = 0
        for crop in CropType:
            if crop not in CropTypePerCategory.silage_crop:
                for harvest_method in HarvestMethod:
                    if harvest_method not in [
                        HarvestMethod.GreenManure,
                        HarvestMethod.Silage,
                        HarvestMethod.Swathing
                    ]:
                        self.land_management_base.crop_type.value = crop
                        self.land_management_base.harvest_method.value = harvest_method
                        self.land_management_base.set_moisture_content()
                        self.assertEqual(
                            12,
                            self.land_management_base.moisture_content_of_crop_percentage.value)

    def run_test_set_percentage_returns(
            self,
            expected_percentage_of_product_yield_returned_to_soil,
            expected_percentage_of_straw_returned_to_soil,
            expected_percentage_of_roots_returned_to_soil
    ):
        self.assertEqual(
            expected_percentage_of_product_yield_returned_to_soil,
            self.land_management_base.percentage_of_product_yield_returned_to_soil.value)
        self.assertEqual(
            expected_percentage_of_straw_returned_to_soil,
            self.land_management_base.percentage_of_straw_returned_to_soil.value)
        self.assertEqual(
            expected_percentage_of_roots_returned_to_soil,
            self.land_management_base.percentage_of_roots_returned_to_soil.value)

    def test_set_percentage_returns_for_perennial_crops(self):
        for crop_type in CropType:
            if not any([
                crop_type.is_annual(),
                crop_type.is_root_crop(),
                crop_type.is_cover_crop(),
                crop_type.is_silage_crop()
            ]):
                for harvest_method in HarvestMethod:
                    if harvest_method not in [
                        HarvestMethod.GreenManure,
                        HarvestMethod.Silage,
                        HarvestMethod.Swathing
                    ]:
                        self.land_management_base.crop_type.value = crop_type
                        self.land_management_base.harvest_method.value = harvest_method
                        self.land_management_base.set_percentage_returns()
                        self.run_test_set_percentage_returns(
                            expected_percentage_of_product_yield_returned_to_soil=Defaults.PercentageOfProductReturnedToSoilForPerennials,
                            expected_percentage_of_straw_returned_to_soil=0,
                            expected_percentage_of_roots_returned_to_soil=Defaults.PercentageOfRootsReturnedToSoilForPerennials)

    def test_set_percentage_returns_for_annual_crops(self):
        for crop_type in CropType:
            if not any([
                crop_type.is_perennial(),
                crop_type.is_root_crop(),
                crop_type.is_cover_crop(),
                crop_type.is_silage_crop()
            ]):
                for harvest_method in HarvestMethod:
                    if harvest_method not in [
                        HarvestMethod.GreenManure,
                        HarvestMethod.Silage,
                        HarvestMethod.Swathing
                    ]:
                        self.land_management_base.crop_type.value = crop_type
                        self.land_management_base.harvest_method.value = harvest_method
                        self.land_management_base.set_percentage_returns()
                        self.run_test_set_percentage_returns(
                            expected_percentage_of_product_yield_returned_to_soil=Defaults.PercentageOfProductReturnedToSoilForAnnuals,
                            expected_percentage_of_straw_returned_to_soil=Defaults.PercentageOfStrawReturnedToSoilForAnnuals,
                            expected_percentage_of_roots_returned_to_soil=Defaults.PercentageOfRootsReturnedToSoilForAnnuals)

    def test_set_percentage_returns_for_root_crops(self):
        for crop_type in CropType:
            if not any([
                crop_type.is_perennial(),
                crop_type.is_annual(),
                crop_type.is_cover_crop(),
                crop_type.is_silage_crop()
            ]):
                for harvest_method in HarvestMethod:
                    if harvest_method not in [
                        HarvestMethod.GreenManure,
                        HarvestMethod.Silage,
                        HarvestMethod.Swathing
                    ]:
                        self.land_management_base.crop_type.value = crop_type
                        self.land_management_base.harvest_method.value = harvest_method
                        self.land_management_base.set_percentage_returns()
                        self.run_test_set_percentage_returns(
                            expected_percentage_of_product_yield_returned_to_soil=Defaults.PercentageOfProductReturnedToSoilForRootCrops,
                            expected_percentage_of_straw_returned_to_soil=Defaults.PercentageOfStrawReturnedToSoilForRootCrops,
                            expected_percentage_of_roots_returned_to_soil=0)

    def test_set_percentage_returns_for_cover_crops(self):
        for crop_type in CropType:
            if not any([
                crop_type.is_perennial(),
                crop_type.is_annual(),
                crop_type.is_root_crop(),
                crop_type.is_silage_crop()
            ]):
                for harvest_method in HarvestMethod:
                    if harvest_method not in [
                        HarvestMethod.GreenManure,
                        HarvestMethod.Silage,
                        HarvestMethod.Swathing
                    ]:
                        self.land_management_base.crop_type.value = crop_type
                        self.land_management_base.harvest_method.value = harvest_method
                        self.land_management_base.set_percentage_returns()
                        self.run_test_set_percentage_returns(
                            expected_percentage_of_product_yield_returned_to_soil=100,
                            expected_percentage_of_straw_returned_to_soil=100,
                            expected_percentage_of_roots_returned_to_soil=100)

    def test_set_percentage_returns_for_silage_crops(self):
        for crop_type in CropType:
            if not any([
                crop_type.is_perennial(),
                crop_type.is_annual(),
                crop_type.is_root_crop(),
                crop_type.is_cover_crop()
            ]):
                for harvest_method in HarvestMethod:
                    if harvest_method not in [
                        HarvestMethod.GreenManure,
                        HarvestMethod.Silage,
                        HarvestMethod.Swathing
                    ]:
                        self.land_management_base.crop_type.value = crop_type
                        self.land_management_base.harvest_method.value = harvest_method
                        self.land_management_base.set_percentage_returns()
                        self.run_test_set_percentage_returns(
                            expected_percentage_of_product_yield_returned_to_soil=2,
                            expected_percentage_of_straw_returned_to_soil=0,
                            expected_percentage_of_roots_returned_to_soil=100)

    def test_set_percentage_returns_for_silage_harvest_method(self):
        for crop_type in CropType:
            self.land_management_base.crop_type.value = crop_type
            self.land_management_base.harvest_method.value = HarvestMethod.Silage
            self.land_management_base.set_percentage_returns()
            self.run_test_set_percentage_returns(
                expected_percentage_of_product_yield_returned_to_soil=2,
                expected_percentage_of_straw_returned_to_soil=0,
                expected_percentage_of_roots_returned_to_soil=100)

    def test_set_percentage_returns_for_swathing_harvest_method(self):
        for crop_type in CropType:
            if not crop_type.is_silage_crop():
                self.land_management_base.crop_type.value = crop_type
                self.land_management_base.harvest_method.value = HarvestMethod.Swathing
                self.land_management_base.set_percentage_returns()
                self.run_test_set_percentage_returns(
                    expected_percentage_of_product_yield_returned_to_soil=30,
                    expected_percentage_of_straw_returned_to_soil=0,
                    expected_percentage_of_roots_returned_to_soil=100)

    def test_set_percentage_returns_for_green_manure_harvest_method(self):
        for crop_type in CropType:
            if not crop_type.is_silage_crop():
                self.land_management_base.crop_type.value = crop_type
                self.land_management_base.harvest_method.value = HarvestMethod.GreenManure
                self.land_management_base.set_percentage_returns()
                self.run_test_set_percentage_returns(
                    expected_percentage_of_product_yield_returned_to_soil=100,
                    expected_percentage_of_straw_returned_to_soil=0,
                    expected_percentage_of_roots_returned_to_soil=100)


if __name__ == '__main__':
    unittest.main()
