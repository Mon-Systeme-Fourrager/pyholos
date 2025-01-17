import unittest
from random import random

from holos_service.components.land_management.carbon.relative_biomass_information import (
    parse_irrigation_data, parse_province_data, parse_carbon_residue_data)
from holos_service.components.land_management.common import IrrigationType
from holos_service.django_stuff import CanadianProvince


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
            self.assertEqual(
                expected,
                list(parse_irrigation_data(raw_input=raw_input).__dict__.values()))


class TestParseProvinceData(unittest.TestCase):

    def test_values(self):
        for raw_input, expected in [
            ("<200 mm", None),
            ("<350", None),
            (">200mm", None),
            (">350 mm", None),
            (">750", None),
            ("200 -350 mm", None),
            ("350-750", None),
            ("AB", CanadianProvince.Alberta),
            ("Canada", None),
            ("Irrigated", None),
            ("Rainfed", None)
        ]:
            self.assertEqual(
                expected,
                parse_province_data(raw_input=raw_input))


class TestParseCarbonResidueData(unittest.TestCase):
    def test_all_filled_columns(self):
        self.assertNotIn(
            None,
            parse_carbon_residue_data(raw_inputs=[str(v) for v in [random()] * 4]).__dict__.values())

    def test_columns_include_empty_column(self):
        for i in range(4):
            base_columns = [str(v) for v in [random()] * 3]
            base_columns.insert(i, "")
            self.assertEqual(
                None,
                list(parse_carbon_residue_data(raw_inputs=base_columns).__dict__.values())[i])

    def test_all_empty_columns(self):
        self.assertEqual(
            {None},
            set(parse_carbon_residue_data(raw_inputs=[''] * 4).__dict__.values()))


if __name__ == '__main__':
    unittest.main()
