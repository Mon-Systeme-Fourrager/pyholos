import unittest

from holos_service.components.land_management import field_system
from holos_service.components.land_management.common import HarvestMethod
from holos_service.components.land_management.crop import CropType


class TestLandManagementBase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.silage_crop = [
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
        for crop_type in self.silage_crop:
            self.land_management_base.crop_type.value = crop_type
            self.assertEqual(
                HarvestMethod.Silage,
                self.land_management_base.get_default_harvest_method())

    def test_get_default_harvest_method_for_non_silage_crops(self):
        for crop_type in CropType:
            if crop_type not in self.silage_crop:
                self.land_management_base.crop_type.value = crop_type
                self.assertEqual(
                    HarvestMethod.CashCrop,
                    self.land_management_base.get_default_harvest_method())


if __name__ == '__main__':
    unittest.main()
