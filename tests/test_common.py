import unittest

from holos_service import common
from holos_service.django_stuff import CanadianProvince


class TestGetRegion(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.west_region_provinces = (
            CanadianProvince.Alberta,
            CanadianProvince.BritishColumbia,
            CanadianProvince.Manitoba,
            CanadianProvince.Saskatchewan,
            CanadianProvince.NorthwestTerritories,
            CanadianProvince.Nunavut)

    def test_west_region(self):
        for province in self.west_region_provinces:
            self.assertEqual(
                common.Region.WesternCanada,
                common.get_region(province=province.name))

    def test_east_region(self):
        for province in CanadianProvince:
            if province not in self.west_region_provinces:
                self.assertEqual(
                    common.Region.EasternCanada,
                    common.get_region(province=province.name))


if __name__ == '__main__':
    unittest.main()
