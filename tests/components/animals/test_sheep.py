import unittest

from holos_service.components.animals import sheep
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


if __name__ == '__main__':
    unittest.main()
