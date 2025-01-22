import unittest

from holos_service.components.land_management import common


class TestConvertTillageTypeName(unittest.TestCase):
    def test_values_for_not_till(self):
        for s in ("notill", "nt"):
            self.assertEqual(
                common.TillageType.NoTill,
                common.convert_tillage_type_name(name=s))

    def test_values_for_reduced_tillage(self):
        for s in ("reduced", "rt"):
            self.assertEqual(
                common.TillageType.Reduced,
                common.convert_tillage_type_name(name=s))

    def test_values_for_intensive_tillage(self):
        for s in ("intensive", "it", "conventional"):
            self.assertEqual(
                common.TillageType.Intensive,
                common.convert_tillage_type_name(name=s))

    def test_values_for_unrecognisable_text(self):
        for s in ("some", "random", "name"):
            self.assertEqual(
                None,
                common.convert_tillage_type_name(name=s))


if __name__ == '__main__':
    unittest.main()
