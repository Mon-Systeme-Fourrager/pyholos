import unittest

from holos_service.components.animals import common


class TestHousingTypeExtensions(unittest.TestCase):
    def test_is_free_stall(self):
        housing_type = common.HousingType.small_free_stall
        ext = common.HousingTypeExtensions(housing_type)

        self.assertTrue(ext.is_free_stall)
        self.assertTrue(ext.is_electrical_consuming_housing_type)

        self.assertFalse(ext.is_tie_stall)
        self.assertFalse(ext.is_barn)
        self.assertFalse(ext.is_feed_lot)
        self.assertFalse(ext.is_indoor_housing)
        self.assertFalse(ext.is_pasture)

    def test_is_tie_stall(self):
        housing_type = common.HousingType.tie_stall
        ext = common.HousingTypeExtensions(housing_type)

        self.assertTrue(ext.is_tie_stall)
        self.assertTrue(ext.is_electrical_consuming_housing_type)

        self.assertFalse(ext.is_free_stall)
        self.assertFalse(ext.is_barn)
        self.assertFalse(ext.is_feed_lot)
        self.assertFalse(ext.is_indoor_housing)
        self.assertFalse(ext.is_pasture)

    def test_is_barn(self):
        housing_type = common.HousingType.housed_in_barn
        ext = common.HousingTypeExtensions(housing_type)

        self.assertTrue(ext.is_barn)
        self.assertTrue(ext.is_indoor_housing)
        self.assertTrue(ext.is_electrical_consuming_housing_type)

        self.assertFalse(ext.is_free_stall)
        self.assertFalse(ext.is_tie_stall)
        self.assertFalse(ext.is_feed_lot)
        self.assertFalse(ext.is_pasture)

    def test_is_feed_lot(self):
        housing_type = common.HousingType.confined
        ext = common.HousingTypeExtensions(housing_type)

        self.assertTrue(ext.is_feed_lot)
        self.assertTrue(ext.is_electrical_consuming_housing_type)

        self.assertFalse(ext.is_free_stall)
        self.assertFalse(ext.is_tie_stall)
        self.assertFalse(ext.is_barn)
        self.assertFalse(ext.is_indoor_housing)
        self.assertFalse(ext.is_pasture)

    def test_is_pasture(self):
        housing_type = common.HousingType.pasture
        ext = common.HousingTypeExtensions(housing_type)

        self.assertTrue(ext.is_pasture)

        self.assertFalse(ext.is_free_stall)
        self.assertFalse(ext.is_tie_stall)
        self.assertFalse(ext.is_barn)
        self.assertFalse(ext.is_feed_lot)
        self.assertFalse(ext.is_electrical_consuming_housing_type)
        self.assertFalse(ext.is_indoor_housing)


if __name__ == '__main__':
    unittest.main()
