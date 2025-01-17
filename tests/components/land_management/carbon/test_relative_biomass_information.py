import unittest
from random import random, randint, choice

from holos_service.components.land_management.carbon.relative_biomass_information import (
    parse_irrigation_data, parse_province_data, parse_carbon_residue_data, parse_nitrogen_residue_data,
    parse_lignin_content_data, parse_biomethane_data, RelativeBiomassInformationData,
    BiogasAndMethaneProductionParametersData, parse_relative_biomass_information_data)
from holos_service.components.land_management.common import IrrigationType
from holos_service.components.land_management.crop import CropType
from holos_service.config import PathsHolosResources
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


class TestParseNitrogenResidueData(unittest.TestCase):
    def test_all_filled_columns(self):
        self.assertNotIn(
            None,
            parse_nitrogen_residue_data(raw_inputs=[str(v) for v in [randint(0, 100)] * 3]).__dict__.values())

    def test_columns_include_empty_column(self):
        for i in range(4):
            base_columns = [str(v) for v in [randint(0, 100)] * 2]
            base_columns.insert(i, "")
            self.assertEqual(
                None,
                list(parse_nitrogen_residue_data(raw_inputs=base_columns).__dict__.values())[i])

    def test_all_empty_columns(self):
        self.assertEqual(
            {None},
            set(parse_nitrogen_residue_data(raw_inputs=[''] * 3).__dict__.values()))


class TestParseLigninContentData(unittest.TestCase):
    def test_filled_column(self):
        self.assertNotEqual(
            None,
            parse_lignin_content_data(raw_input=str(random())))

    def test_empty_column(self):
        self.assertEqual(
            None,
            parse_lignin_content_data(raw_input=""))


class TestParseBiomethaneData(unittest.TestCase):
    def test_all_filled_columns(self):
        self.assertNotIn(
            None,
            parse_biomethane_data(
                crop_type=choice(list(CropType)),
                raw_inputs=[str(v) for v in [random()] * 5]).__dict__.values()
        )

    def test_columns_include_empty_column(self):
        for i in range(4):
            base_columns = [str(v) for v in [random()] * 4]
            base_columns.insert(i, "")
            self.assertEqual(
                None,
                list(parse_biomethane_data(
                    crop_type=choice(list(CropType)),
                    raw_inputs=base_columns).__dict__.values())[i + 1])

    def test_all_empty_columns(self):
        self.assertEqual(
            {None},
            set(list(parse_biomethane_data(
                crop_type=choice(list(CropType)),
                raw_inputs=[''] * 5).__dict__.values())[1:]))


class TestParseRelativeBiomassInformationData(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(PathsHolosResources.Table_7_Relative_Biomass_Information, mode='r') as f:
            with PathsHolosResources.Table_7_Relative_Biomass_Information.open(mode='r') as f:
                cls.lines = [l for l in f.readlines()[5:] if all([
                    not len(l.replace(' ', '').replace(',', '').replace('\n', '')) == 0,
                    not l.startswith('#')
                ])][2:]

    def test_summer_fallow(self):
        crop_type = CropType.SummerFallow
        actual = parse_relative_biomass_information_data(raw_input=self.lines[0])
        expected = RelativeBiomassInformationData(
            crop_type=crop_type,
            irrigation_type=None,
            irrigation_lower_range_limit=0,
            irrigation_upper_range_limit=0,
            moisture_content_of_product=0,
            relative_biomass_product=0,
            relative_biomass_straw=0,
            relative_biomass_root=0,
            relative_biomass_extraroot=0,
            nitrogen_content_product=0,
            nitrogen_content_straw=0,
            nitrogen_content_root=0,
            nitrogen_content_extraroot=0,
            lignin_content=0,
            province=None,
            biogas_and_methane_production_parameters_data=BiogasAndMethaneProductionParametersData(
                crop_type=crop_type,
                bio_methane_potential=0,
                methane_fraction=0,
                volatile_solids=0,
                total_solids=0,
                total_nitrogen=0
            ))
        self.assertDictEqual(actual.__dict__, expected.__dict__)

    def test_barley_high_irrigation_rate(self):
        crop_type = CropType.Barley
        actual = parse_relative_biomass_information_data(raw_input=self.lines[7])
        expected = RelativeBiomassInformationData(
            crop_type=crop_type,
            irrigation_type=None,
            irrigation_lower_range_limit=750,
            irrigation_upper_range_limit=float('inf'),
            moisture_content_of_product=12,
            relative_biomass_product=0.424,
            relative_biomass_straw=0.498,
            relative_biomass_root=0.047,
            relative_biomass_extraroot=0.031,
            nitrogen_content_product=19,
            nitrogen_content_straw=3.8,
            nitrogen_content_root=9.5,
            nitrogen_content_extraroot=9.5,
            lignin_content=0.046,
            province=None,
            biogas_and_methane_production_parameters_data=BiogasAndMethaneProductionParametersData(
                crop_type=crop_type,
                bio_methane_potential=267,
                methane_fraction=0.44,
                volatile_solids=90,
                total_solids=880,
                total_nitrogen=6.1
            ))
        self.assertDictEqual(actual.__dict__, expected.__dict__)

    def test_canola_medium_irrigation_rate(self):
        crop_type = CropType.Canola
        actual = parse_relative_biomass_information_data(raw_input=self.lines[30])
        expected = RelativeBiomassInformationData(
            crop_type=crop_type,
            irrigation_type=None,
            irrigation_lower_range_limit=200,
            irrigation_upper_range_limit=350,
            moisture_content_of_product=9,
            relative_biomass_product=0.176,
            relative_biomass_straw=0.529,
            relative_biomass_root=0.183,
            relative_biomass_extraroot=0.111,
            nitrogen_content_product=62.1,
            nitrogen_content_straw=9.9,
            nitrogen_content_root=13.4,
            nitrogen_content_extraroot=13.4,
            lignin_content=0.073,
            province=None,
            biogas_and_methane_production_parameters_data=BiogasAndMethaneProductionParametersData(
                crop_type=crop_type,
                bio_methane_potential=0,
                methane_fraction=0,
                volatile_solids=0,
                total_solids=0,
                total_nitrogen=0
            ))
        self.assertDictEqual(actual.__dict__, expected.__dict__)

    def test_berries_and_grapes_canada(self):
        crop_type = CropType.BerriesAndGrapes
        actual = parse_relative_biomass_information_data(raw_input=self.lines[53])
        expected = RelativeBiomassInformationData(
            crop_type=crop_type,
            irrigation_type=None,
            irrigation_lower_range_limit=0,
            irrigation_upper_range_limit=0,
            moisture_content_of_product=85,
            relative_biomass_product=0,
            relative_biomass_straw=0,
            relative_biomass_root=0,
            relative_biomass_extraroot=0,
            nitrogen_content_product=7,
            nitrogen_content_straw=20,
            nitrogen_content_root=10,
            nitrogen_content_extraroot=10,
            lignin_content=0,
            province=None,
            biogas_and_methane_production_parameters_data=BiogasAndMethaneProductionParametersData(
                crop_type=crop_type,
                bio_methane_potential=0,
                methane_fraction=0,
                volatile_solids=0,
                total_solids=0,
                total_nitrogen=0
            ))
        self.assertDictEqual(actual.__dict__, expected.__dict__)

    def test_oat_avena_sativa(self):
        crop_type = CropType.OatAvenaSativa
        actual = parse_relative_biomass_information_data(raw_input=self.lines[71])
        expected = RelativeBiomassInformationData(
            crop_type=crop_type,
            irrigation_type=None,
            irrigation_lower_range_limit=0,
            irrigation_upper_range_limit=0,
            moisture_content_of_product=65,
            relative_biomass_product=0.737,
            relative_biomass_straw=0,
            relative_biomass_root=0.16,
            relative_biomass_extraroot=0.104,
            nitrogen_content_product=24.3,
            nitrogen_content_straw=0,
            nitrogen_content_root=15.7,
            nitrogen_content_extraroot=15.7,
            lignin_content=0.047,
            province=None,
            biogas_and_methane_production_parameters_data=BiogasAndMethaneProductionParametersData(
                crop_type=crop_type,
                bio_methane_potential=0,
                methane_fraction=0,
                volatile_solids=0,
                total_solids=0,
                total_nitrogen=0
            ))
        self.assertDictEqual(actual.__dict__, expected.__dict__)

    def test_sesame_sesamum_indicum(self):
        crop_type = CropType.SesameSesamumIndicum
        actual = parse_relative_biomass_information_data(raw_input=self.lines[73])
        expected = RelativeBiomassInformationData(
            crop_type=crop_type,
            irrigation_type=None,
            irrigation_lower_range_limit=0,
            irrigation_upper_range_limit=0,
            moisture_content_of_product=65,
            relative_biomass_product=0,
            relative_biomass_straw=0,
            relative_biomass_root=0,
            relative_biomass_extraroot=0,
            nitrogen_content_product=0,
            nitrogen_content_straw=12.2,
            nitrogen_content_root=0,
            nitrogen_content_extraroot=0,
            lignin_content=0.053,
            province=None,
            biogas_and_methane_production_parameters_data=BiogasAndMethaneProductionParametersData(
                crop_type=crop_type,
                bio_methane_potential=0,
                methane_fraction=0,
                volatile_solids=0,
                total_solids=0,
                total_nitrogen=0
            ))
        self.assertDictEqual(actual.__dict__, expected.__dict__)

    def test_shepherds_purse(self):
        crop_type = CropType.ShepherdsPurse
        actual = parse_relative_biomass_information_data(raw_input=self.lines[79])
        expected = RelativeBiomassInformationData(
            crop_type=crop_type,
            irrigation_type=None,
            irrigation_lower_range_limit=0,
            irrigation_upper_range_limit=0,
            moisture_content_of_product=65,
            relative_biomass_product=0.352,
            relative_biomass_straw=0,
            relative_biomass_root=0.393,
            relative_biomass_extraroot=0.255,
            nitrogen_content_product=16.3,
            nitrogen_content_straw=0,
            nitrogen_content_root=9.4,
            nitrogen_content_extraroot=9.4,
            lignin_content=0.075,
            province=None,
            biogas_and_methane_production_parameters_data=BiogasAndMethaneProductionParametersData(
                crop_type=crop_type,
                bio_methane_potential=0,
                methane_fraction=0,
                volatile_solids=0,
                total_solids=0,
                total_nitrogen=0
            ))
        self.assertDictEqual(actual.__dict__, expected.__dict__)


if __name__ == '__main__':
    unittest.main()
