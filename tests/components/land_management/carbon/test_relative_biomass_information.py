import unittest

from holos_service.components.land_management.carbon.relative_biomass_information import parse_irrigation_data
from holos_service.components.land_management.common import IrrigationType


class TestParseIrrigationData(unittest.TestCase):

    def test_values(self):
        float_inf = float('inf')
        for raw_input, expected in [
            ("<200 mm", [None, 0, 200]),
            ("<350", [None, 0, 350]),
            (">200mm", [None, 200, float_inf]),
            (">350 mm", [None, 350, float_inf]),
            (">750", [None, 750, float_inf]),
            ("200 -350 mm", [None, 200, 350]),
            ("350-750", [None, 350, 750]),
            ("AB", [None, None, None]),
            ("Canada", [None, None, None]),
            ("Irrigated", [IrrigationType.Irrigated, None, None]),
            ("Rainfed", [IrrigationType.RainFed, None, None])
        ]:
            print(raw_input)
            self.assertEqual(
                expected,
                list(parse_irrigation_data(raw_input=raw_input).__dict__.values()))


if __name__ == '__main__':
    unittest.main()
