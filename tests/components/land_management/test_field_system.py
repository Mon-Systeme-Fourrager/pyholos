import unittest
from itertools import product

from holos_service.components.land_management import field_system
from holos_service.components.land_management.common import HarvestMethod, IrrigationType
from holos_service.components.land_management.crop import CropType


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
        for crop_type in self.silage_crops:
            self.land_management_base.crop_type.value = crop_type
            self.assertEqual(
                HarvestMethod.Silage,
                self.land_management_base.get_default_harvest_method())

    def test_get_default_harvest_method_for_non_silage_crops(self):
        for crop_type in CropType:
            if crop_type not in self.silage_crops:
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
        for crop, harvest_method in product(self.silage_crops, [
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
            if crop not in self.silage_crops:
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
            if crop not in self.silage_crops:
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


if __name__ == '__main__':
    unittest.main()
