import unittest
from pathlib import Path
from shutil import rmtree

from holos_service import launching


class TestLaunching(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.path_sources = Path(__file__).parent / 'sources'
        cls.path_holos_cli = cls.path_sources / 'holos_cli.lnk'
        cls.path_dir_farms = cls.path_sources / 'farms'
        cls.path_dir_outputs = cls.path_dir_farms / 'Outputs_complete_inputs'
        cls.name_farm_json = 'farm.json'
        cls.name_dir_farms_json = None
        cls.name_settings = None
        cls.id_slc_polygon = 851003
        cls.timeout_secs = 60
        cls.expected_output_folders = ['farm_from_json', 'HolosExampleFarm', 'Outputs_complete_inputs']


    @classmethod
    def tearDownClass(cls):
        for f in cls.path_dir_farms.iterdir():
            if f.is_dir() and f.name.startswith(('farm_from_json', 'HolosExampleFarm', 'Outputs')):
                rmtree(f)

    def test_create_farm_files_from_json_with_complete_inputs(self):
        launching.launch_holos(
            path_holos_cli=self.path_holos_cli,
            path_dir_farms=self.path_dir_farms,
            name_farm_json=self.name_farm_json,
            name_dir_farms_json=self.name_dir_farms_json,
            name_settings=self.name_settings,
            path_dir_outputs=self.path_dir_outputs,
            id_slc_polygon=self.id_slc_polygon)

        outputs = [v.name for v in self.path_dir_farms.iterdir() if v.is_dir()]
        self.assertEqual(outputs, self.expected_output_folders)
        for f in ('farm_from_json_Results', 'TotalResultsForAllFarms'):
            self.assertTrue((self.path_dir_outputs / 'Outputs' / f).is_dir())

    def test_run_on_existing_farm_data(self):
        launching.launch_holos(
            path_holos_cli=self.path_holos_cli,
            path_dir_farms=self.path_dir_farms,
            name_farm_json=None,
            name_dir_farms_json=None,
            name_settings=None,
            path_dir_outputs=None,
            id_slc_polygon=None)

        outputs = [v.name for v in self.path_dir_farms.iterdir() if v.is_dir()]
        self.assertEqual(sorted(outputs), sorted(self.expected_output_folders))
        for f in ('farm_from_json_Results', 'TotalResultsForAllFarms'):
            self.assertTrue((self.path_dir_farms / 'Outputs' / f).is_dir())


if __name__ == '__main__':
    unittest.main()
