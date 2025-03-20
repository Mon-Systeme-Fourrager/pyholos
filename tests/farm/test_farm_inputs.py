import unittest
from math import inf
from random import uniform
from uuid import UUID

from pydantic import ValidationError

from holos_service.components.land_management.crop import CropType
from holos_service.farm import farm_inputs


class TestCalcYearInPerennialStand(unittest.TestCase):
    @staticmethod
    def calc_year_in_perennial_stand(**kwargs):
        return farm_inputs.FieldsInput.calc_year_in_perennial_stand(**kwargs)

    def test_all_annual(self):
        crops = [
            CropType.Wheat,
            CropType.Corn,
            CropType.Barley
        ]
        self.assertEqual(
            [0] * len(crops),
            self.calc_year_in_perennial_stand(crops=crops))

    def test_all_perennial(self):
        crops = [
            CropType.TameMixed,
            CropType.TameMixed,
            CropType.TameMixed
        ]
        self.assertEqual(
            [v + 1 for v in range(len(crops))],
            self.calc_year_in_perennial_stand(crops=crops))

    def test_mixed_annual_and_perennial(self):
        crops, expected = zip(*[
            (CropType.Wheat, 0),
            (CropType.Barley, 0),
            (CropType.TameMixed, 1),
            (CropType.TameMixed, 2),
            (CropType.TameMixed, 3),
            (CropType.Corn, 0)
        ])
        self.assertEqual(
            list(expected),
            self.calc_year_in_perennial_stand(crops=crops))


class TestCalcPerennialStandLengths(unittest.TestCase):
    @staticmethod
    def calc_perennial_stand_lengths(**kwargs):
        return farm_inputs.FieldsInput.calc_perennial_stand_lengths(**kwargs)

    def run_test(
            self,
            years_data: list[int] | tuple[int, ...],
            expected: list[int] | tuple[int, ...],
    ):
        self.assertEqual(
            list(expected),
            self.calc_perennial_stand_lengths(years_in_perennial_stand=years_data))

    def test_all_annual(self):
        years_data, expected = zip(*[
            (0, 1),
            (0, 1),
            (0, 1)
        ])
        self.run_test(
            expected=expected,
            years_data=years_data)

    def test_all_perennial(self):
        years_data, expected = zip(*[
            (1, 4),
            (2, 4),
            (3, 4),
            (4, 4),
        ])
        self.run_test(
            expected=expected,
            years_data=years_data)

    def test_mixed_annual_and_perennial(self):
        years_data, expected = zip(*[
            (0, 1),
            (1, 1),
            (0, 1),
            (1, 3),
            (2, 3),
            (3, 3),
            (0, 1),
        ])
        self.run_test(
            expected=expected,
            years_data=years_data)


class TestSetPerennialStandId(unittest.TestCase):
    @staticmethod
    def set_perennial_stand_id(**kwargs):
        return farm_inputs.FieldsInput.set_perennial_stand_id(**kwargs)

    @classmethod
    def setUpClass(cls):
        cls.id_for_annual = UUID("00000000-0000-0000-0000-000000000000")

    def test_all_annual(self):
        crops = [
            CropType.Wheat,
            CropType.Wheat,
            CropType.Wheat,
        ]
        self.assertEqual(
            [self.id_for_annual] * len(crops),
            self.set_perennial_stand_id(crops=crops))

    def test_all_perennial(self):
        crops = [
            CropType.TameMixed,
            CropType.TameMixed,
            CropType.TameMixed
        ]

        ids_perennial = self.set_perennial_stand_id(crops=crops)
        for id_result in ids_perennial:
            self.assertNotEqual(
                self.id_for_annual,
                id_result)
        self.assertEqual(
            list(set(ids_perennial))[0],
            ids_perennial[0])

    def test_mixed_annual_and_perennial(self):
        crops = [
            CropType.Wheat,
            CropType.Barley,
            CropType.TameMixed,
            CropType.TameMixed,
            CropType.TameMixed,
            CropType.Corn,
        ]

        ids_perennial = self.set_perennial_stand_id(crops=crops)
        for crop, id_result in zip(crops, ids_perennial):
            if crop.is_perennial():
                self.assertNotEqual(
                    self.id_for_annual,
                    id_result)
            else:
                self.assertEqual(
                    self.id_for_annual,
                    id_result)
        self.assertEqual(
            2,
            len(set(ids_perennial)))

    def test_mixed_perennial_crops(self):
        crops = [
            CropType.TameMixed,
            CropType.TameMixed,
            CropType.TameMixed,
            CropType.Forage,
            CropType.Forage,
            CropType.Forage,
        ]

        ids_perennial = self.set_perennial_stand_id(crops=crops)
        unique_ids = set(ids_perennial)
        for id_result in unique_ids:
            self.assertNotEqual(
                self.id_for_annual,
                id_result)

        self.assertEqual(
            2,
            len(unique_ids))


class TestInputWeatherData(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.WeatherData = farm_inputs.WeatherData
        cls.year = 2025
        cls.precipitation = [uniform(0, 100) for _ in range(366)]
        cls.potential_evapotranspiration = [uniform(0, 100) for _ in range(366)]
        cls.temperature = [uniform(-30, 35) for _ in range(366)]

    def test_works_with_correct_types_and_values(self):
        self.WeatherData(
            year=self.year,
            precipitation=self.precipitation,
            potential_evapotranspiration=self.potential_evapotranspiration,
            temperature=self.temperature)

    def test_erroneous_year_input(self):
        kwargs = dict(
            precipitation=self.precipitation,
            potential_evapotranspiration=self.potential_evapotranspiration,
            temperature=self.temperature)

        for year, expected_message in [
            (-1, 'Input should be greater than 1970'),
            (None, 'Input should be a valid integer'),
            (inf, 'Input should be a finite number'),
            (-inf, 'Input should be a finite number'),
            ('', 'Input should be a valid integer, unable to parse string as an integer'),
        ]:
            try:
                self.WeatherData(year=year, **kwargs)
            except ValidationError as e:
                self.assertEqual(expected_message, e.errors()[0]['msg'])

    def test_erroneous_precipitation_input(self):
        kwargs = dict(
            year=self.year,
            potential_evapotranspiration=self.potential_evapotranspiration,
            temperature=self.temperature)

        for precipitation, expected_message in [
            (self.precipitation[10:], 'List should have at least 365 items after validation, not 356'),
            (self.precipitation[:-1] + [-1], 'Input should be greater than or equal to 0'),
            (self.precipitation[:-1] + [None], 'Input should be a valid number'),
            (self.precipitation[:-1] + [inf], 'Input should be a finite number'),
            (self.precipitation[:-1] + [-inf], 'Input should be a finite number'),
            (self.precipitation[:-1] + [''], 'Input should be a valid number')
        ]:
            try:
                self.WeatherData(precipitation=precipitation, **kwargs)
            except ValidationError as e:
                self.assertEqual(expected_message, e.errors()[0]['msg'])

    def test_erroneous_potential_evapotranspiration_input(self):
        kwargs = dict(
            year=self.year,
            precipitation=self.precipitation,
            temperature=self.temperature)

        for potential_evapotranspiration, expected_message in [
            (self.potential_evapotranspiration[10:], 'List should have at least 365 items after validation, not 356'),
            (self.potential_evapotranspiration[:-1] + [-1], 'Input should be greater than or equal to 0'),
            (self.potential_evapotranspiration[:-1] + [None], 'Input should be a valid number'),
            (self.potential_evapotranspiration[:-1] + [inf], 'Input should be a finite number'),
            (self.potential_evapotranspiration[:-1] + [-inf], 'Input should be a finite number'),
            (self.potential_evapotranspiration[:-1] + [''], 'Input should be a valid number')
        ]:
            try:
                self.WeatherData(potential_evapotranspiration=potential_evapotranspiration, **kwargs)
            except ValidationError as e:
                self.assertEqual(expected_message, e.errors()[0]['msg'])

    def test_erroneous_temperature_input(self):
        kwargs = dict(
            year=self.year,
            precipitation=self.precipitation,
            potential_evapotranspiration=self.potential_evapotranspiration)

        for temperature, expected_message in [
            (self.temperature[10:], 'List should have at least 365 items after validation, not 356'),
            (self.temperature[:-1] + [None], 'Input should be a valid number'),
            (self.temperature[:-1] + [inf], 'Input should be a finite number'),
            (self.temperature[:-1] + [''], 'Input should be a valid number')
        ]:
            try:
                self.WeatherData(temperature=temperature, **kwargs)
            except ValidationError as e:
                self.assertEqual(expected_message, e.errors()[0]['msg'])


class TestInputWeatherSummary(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.WeatherSummary = farm_inputs.WeatherSummary

    @staticmethod
    def get_kwargs() -> dict:
        return dict(
            year=2025,
            mean_annual_precipitation=uniform(0, 1000),
            mean_annual_temperature=uniform(-5, 5),
            mean_annual_evapotranspiration=uniform(0, 1000),
            growing_season_precipitation=uniform(0, 1000),
            growing_season_evapotranspiration=uniform(0, 1000),
            monthly_precipitation=[uniform(0, 100) for _ in range(12)],
            monthly_potential_evapotranspiration=[uniform(0, 100) for _ in range(12)],
            monthly_temperature=[uniform(-30, 30) for _ in range(12)],
        )

    def test_works_with_correct_types_and_values(self):
        self.WeatherSummary(**self.get_kwargs())

    def test_erroneous_year_input(self):
        kwargs = self.get_kwargs()
        kwargs.pop('year')

        for year, expected_message in [
            (-1, 'Input should be greater than 1970'),
            (None, 'Input should be a valid integer'),
            (inf, 'Input should be a finite number'),
            (-inf, 'Input should be a finite number'),
            ('', 'Input should be a valid integer, unable to parse string as an integer'),
        ]:
            try:
                self.WeatherSummary(year=year, **kwargs)
            except ValidationError as e:
                self.assertEqual(expected_message, e.errors()[0]['msg'])

    def test_erroneous_scalar_water_inputs(self):
        for name in [
            "mean_annual_precipitation",
            "mean_annual_evapotranspiration",
            "growing_season_precipitation",
            "growing_season_evapotranspiration"
        ]:
            kwargs = self.get_kwargs()
            kwargs.pop(name)

            for v, expected_message in [
                (-1, 'Input should be greater than or equal to 0'),
                (None, 'Input should be a valid number'),
                (inf, 'Input should be a finite number'),
                (-inf, 'Input should be a finite number'),
                ('', 'Input should be a valid number')
            ]:
                try:
                    self.WeatherSummary(**{name: v}, **kwargs)
                except ValidationError as e:
                    self.assertEqual(expected_message, e.errors()[0]['msg'])

    def test_erroneous_vector_water_inputs(self):
        for name in [
            "monthly_precipitation",
            "monthly_potential_evapotranspiration"
        ]:
            kwargs = self.get_kwargs()
            values = kwargs[name]
            kwargs.pop(name)

            for v, expected_message in [
                (values[10:], 'List should have at least 12 items after validation, not 2'),
                (values[:-1] + [-1], 'Input should be greater than or equal to 0'),
                (values[:-1] + [None], 'Input should be a valid number'),
                (values[:-1] + [inf], 'Input should be a finite number'),
                (values[:-1] + [-inf], 'Input should be a finite number'),
                (values[:-1] + [''], 'Input should be a valid number')
            ]:
                try:
                    self.WeatherSummary(**{name: v}, **kwargs)
                except ValidationError as e:
                    self.assertEqual(expected_message, e.errors()[0]['msg'])

    def test_erroneous_mean_annual_temperature_input(self):
        kwargs = self.get_kwargs()
        kwargs.pop("mean_annual_temperature")

        for temperature, expected_message in [
            (None, 'Input should be a valid number'),
            (inf, 'Input should be a finite number'),
            ('', 'Input should be a valid number')
        ]:
            try:
                self.WeatherSummary(mean_annual_temperature=temperature, **kwargs)
            except ValidationError as e:
                self.assertEqual(expected_message, e.errors()[0]['msg'])

    def test_erroneous_monthly_temperature_input(self):
        kwargs = self.get_kwargs()
        values = kwargs["monthly_temperature"]
        kwargs.pop("monthly_temperature")

        for v, expected_message in [
            (values[10:], 'List should have at least 12 items after validation, not 2'),
            (values[:-1] + [None], 'Input should be a valid number'),
            (values[:-1] + [inf], 'Input should be a finite number'),
            (values[:-1] + [''], 'Input should be a valid number')
        ]:
            try:
                self.WeatherSummary(monthly_temperature=v, **kwargs)
            except ValidationError as e:
                self.assertEqual(expected_message, e.errors()[0]['msg'])


if __name__ == '__main__':
    unittest.main()
