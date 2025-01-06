import unittest

from holos_service.components.animals import sheep, common
from holos_service.config import PathsHolosResources
from holos_service.utils import read_holos_resource_table


class TestGetAnimalCoefficientData(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.animal_coefficients = (read_holos_resource_table(
            path_file=PathsHolosResources.Table_22_Livestock_Coefficients_For_Sheep, index_col='Sheep Class'))
        cls.animal_coefficients.rename(
            columns={v: v.lower().replace(' ', '_') for v in cls.animal_coefficients.columns},
            inplace=True)

    def setUp(self):
        self.sheep = sheep.Sheep()

    def test_get_animal_coefficient_data_for_sheep_feedlot(self):
        self.sheep.group_name.value = sheep.GroupNames.sheep_feedlot.value
        self.assertEqual(
            self.animal_coefficients.loc['Ram'].to_dict(),
            self.sheep.get_animal_coefficient_data().__dict__)

    def test_get_animal_coefficient_data_for_rams(self):
        self.sheep.group_name.value = sheep.GroupNames.rams.value
        self.assertEqual(
            self.animal_coefficients.loc['Ram'].to_dict(),
            self.sheep.get_animal_coefficient_data().__dict__)

    def test_get_animal_coefficient_data_for_ewes(self):
        self.sheep.group_name.value = sheep.GroupNames.ewes.value
        self.assertEqual(
            self.animal_coefficients.loc['Ewe'].to_dict(),
            self.sheep.get_animal_coefficient_data().__dict__)

    def test_get_animal_coefficient_data_for_lambs(self):
        self.sheep.group_name.value = sheep.GroupNames.lambs.value
        self.assertEqual(
            self.animal_coefficients.loc['Weaned Lambs'].to_dict(),
            self.sheep.get_animal_coefficient_data().__dict__)


class TestGetFeedingActivityCoefficient(unittest.TestCase):

    def test_value_for_housed_ewes(self):
        self.assertEqual(
            0.0096,
            sheep.get_feeding_activity_coefficient(housing_type=common.HousingType.housed_ewes))

    def test_value_for_confined_animals(self):
        self.assertEqual(
            0.0067,
            sheep.get_feeding_activity_coefficient(housing_type=common.HousingType.confined))

    def test_value_for_pasture_and_flat_pasture(self):
        for housing_type in (common.HousingType.pasture,
                             common.HousingType.flat_pasture):
            self.assertEqual(
                0.0107,
                sheep.get_feeding_activity_coefficient(housing_type=housing_type))

    def test_value_for_hilly_pasture_or_open_range(self):
        self.assertEqual(
            0.024,
            sheep.get_feeding_activity_coefficient(housing_type=common.HousingType.hilly_pasture_or_open_range))

    def test_z_error(self):
        for housing_type in common.HousingType:
            if housing_type not in [
                common.HousingType.housed_ewes,
                common.HousingType.confined,
                common.HousingType.pasture,
                common.HousingType.flat_pasture,
                common.HousingType.hilly_pasture_or_open_range,
            ]:
                with self.assertRaises(ValueError):
                    sheep.get_feeding_activity_coefficient(housing_type=housing_type)


if __name__ == '__main__':
    unittest.main()
