import unittest
from holos_service.defaults import Defaults


class MyDefaults(unittest.TestCase):
    def test_values(self):
        self.assertEqual(
            Defaults.EmissionFactorForLeachingAndRunoff.value,
            0.011)


if __name__ == '__main__':
    unittest.main()
