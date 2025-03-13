import unittest

from holos_service.defaults import Defaults


class MyDefaults(unittest.TestCase):
    def test_values(self):
        self.assertEqual(
            Defaults.EmissionFactorForLeachingAndRunoff.value,
            0.011)
        self.assertEqual(
            Defaults.PercentageOfProductReturnedToSoilForPerennials.value,
            35)
        self.assertEqual(
            Defaults.PercentageOfRootsReturnedToSoilForPerennials.value,
            100)
        self.assertEqual(
            Defaults.PercentageOfProductReturnedToSoilForAnnuals.value,
            2)
        self.assertEqual(
            Defaults.PercentageOfRootsReturnedToSoilForAnnuals.value,
            100)
        self.assertEqual(
            Defaults.PercentageOfStrawReturnedToSoilForAnnuals.value,
            100)
        self.assertEqual(
            Defaults.PercentageOfProductReturnedToSoilForRootCrops.value,
            0)
        self.assertEqual(
            Defaults.PercentageOfStrawReturnedToSoilForRootCrops.value,
            100)


if __name__ == '__main__':
    unittest.main()
