from json import load
from pathlib import Path
import unittest

from holos_service import soil


class TestSetSoilTextureAccordingToHolos(unittest.TestCase):
    def test_very_coarse(self):
        self.assertEqual(soil.set_soil_texture_according_to_holos('VC'), 'Coarse')

    def test_coarse(self):
        self.assertEqual(soil.set_soil_texture_according_to_holos('C'), 'Coarse')

    def test_moderately_coarse(self):
        self.assertEqual(soil.set_soil_texture_according_to_holos('MC'), 'Coarse')

    def test_medium(self):
        self.assertEqual(soil.set_soil_texture_according_to_holos('M'), 'Medium')

    def test_medium_skeletal(self):
        self.assertEqual(soil.set_soil_texture_according_to_holos('MS'), 'Medium')

    def test_moderately_fine(self):
        self.assertEqual(soil.set_soil_texture_according_to_holos('MF'), 'Fine')

    def test_fine(self):
        self.assertEqual(soil.set_soil_texture_according_to_holos('F'), 'Fine')

    def test_very_fine(self):
        self.assertEqual(soil.set_soil_texture_according_to_holos('VF'), 'Fine')

    def test_fine_skeletal(self):
        self.assertEqual(soil.set_soil_texture_according_to_holos('FS'), 'Fine')

    def test_unknown(self):
        for s in ['CS', 'FR', 'SM', 'SU', 'FI', 'ME', 'HU', 'UD']:
            self.assertEqual(soil.set_soil_texture_according_to_holos(s), 'Medium')


class TestSetSoilProperties(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with (Path(__file__).parent / 'sources/soil_data_example.json').open(mode='r') as f:
            cls.example_data = load(f)['data']

    def test_set_soil_properties_returns_expected_results(self):
        for example_data in self.example_data:
            example_inputs = example_data['inputs']
            self.assertEqual(
                soil.set_soil_properties(
                    latitude=example_inputs['Latitude'],
                    longitude=example_inputs['Longitude'],
                    year_of_observation=2024),
                example_data['outputs'])

if __name__ == '__main__':
    unittest.main()
