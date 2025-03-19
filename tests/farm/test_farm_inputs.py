import unittest
from uuid import UUID

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
            self.calc_perennial_stand_lengths(year_in_perennial_stand=years_data))

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


if __name__ == '__main__':
    unittest.main()
