import unittest
from pathlib import Path

from holos_service import params


class TestFarmSettingsVar(unittest.TestCase):
    def test_farm_settings_variable_works_accepts_any_type_for_values(self):
        for v in (1, 1.0, 'str', Path):
            self.assertEqual(v, params.FarmSettingsVar(name='test_variable', value=v).value)


class TestParamGeneric(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.param_generic = params.ParamGeneric(title='test')

    def test_param_generic_has_expected_title(self):
        self.assertEqual('# test', self.param_generic.title)

    def test_param_generic_method_returns_expected_list(self):
        self.assertEqual(['# test'], self.param_generic.to_list())


class TestParamsFarmSettings(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.params_farm_settings = params.ParamsFarmSettings(
            province='toto',
            year=1,
            polygon_id=1,
            ecodistrict_id=1,
            latitude=1.0,
            longitude=1.0,
            monthly_precipitation=list(range(12)),
            monthly_potential_evapotranspiration=list(range(12)),
            monthly_temperature=list(range(12)),
            run_in_period_years=15,
            soil_great_group='toto',
            soil_functional_category='toto',
            bulk_density=1.,
            soil_texture='toto',
            soil_ph=1.,
            top_layer_thickness=1,
            proportion_of_sand_in_soil=1,
            proportion_of_clay_in_soil=1,
            proportion_of_soil_organic_carbon=1)
        cls.path_farm_settings = Path(__file__).parent / 'sources/Farm.settings'

    @classmethod
    def tearDownClass(cls):
        if cls.path_farm_settings.exists():
            cls.path_farm_settings.unlink()

    def test_params_farm_settings_output_is_written_to_file(self):
        self.params_farm_settings.write(self.path_farm_settings.parent)
        self.assertTrue(self.path_farm_settings.exists())

        expected_output = [
            '# General',
            'Yield Assignment Method = SmallAreaData',
            'Polygon Number = 1',
            'Latitude = 1.0',
            'Longitude = 1.0',
            'Carbon Concentration  (kg kg^-1) = 0.45',
            'Emergence Day = 141',
            'Ripening Day = 197',
            'Variance = 300',
            'Alfa = 0.7',
            'Decomposition Minimum Temperature  (°C) = -3.78',
            'Decomposition Maximum Temperature  (°C)  = 30',
            'Moisture Response Function At Saturation = 0.42',
            'Moisture Response Function At Wilting Point = 0.18',
            '',
            '# Annual Crops',
            'Percentage Of Product Returned To Soil For Annuals = 2',
            'Percentage Of Straw Returned To Soil For Annuals = 100',
            'Percentage Of Roots Returned To Soil For Annuals = 100',
            '',
            '# Silage Crops',
            'Percentage Of Product Yield Returned To Soil For Silage Crops = 35',
            'Percentage Of Roots Returned To Soil For Silage Crops = 100',
            '',
            '# Cover Crops',
            'Percentage Of Product Yield Returned To Soil For Cover Crops = 100',
            'Percentage Of Product Yield Returned To Soil For Cover Crops Forage = 35',
            'Percentage Of Product Yield Returned To Soil For Cover Crops Produce = 0',
            'Percentage Of Straw Returned To Soil For Cover Crops = 100',
            'Percentage Of Roots Returned To Soil For Cover Crops = 100',
            '',
            '# Root Crops',
            'Percentage Of Product Returned To Soil For Root Crops = 0',
            'Percentage Of Straw Returned To Soil For Root Crops = 100',
            '',
            '# Perennial Crops',
            'Percentage Of Product Returned To Soil For Perennials = 35',
            'Percentage Of Roots Returned To Soil For Perennials = 100',
            '',
            '# Rangeland',
            'Percentage Of Product Returned To Soil For Rangeland Due To Harvest Loss = 35',
            'Percentage Of Roots Returned To Soil For Rangeland = 100',
            '',
            '# Fodder Corn',
            'Percentage Of Product Returned To Soil For Fodder Corn = 35',
            'Percentage Of Roots Returned To Soil For Fodder Corn = 100',
            'Decomposition Rate Constant Young Pool = 0.8',
            'Decomposition Rate Constant Old Pool = 0.00605',
            'Old Pool Carbon N = 0.1',
            'NO Ratio = 0.1',
            'Emission Factor For Leaching And Runoff  (kg N2O-N (kg N)^-1) = 0.011',
            'Emission Factor For Volatilization  (kg N2O-N (kg N)^-1) = 0.01',
            'Fraction Of N Lost By Volatilization = 0.21',
            'Microbe Death = 0.2',
            'Denitrification = 0.5',
            'Carbon modelling strategy = ipcctier2',
            'Run In Period Years = 15',
            '',
            '# ICBM/Climate',
            'Humification Coefficient Above Ground = 0.125',
            'Humification Coefficient Below Ground = 0.3',
            'Humification Coefficient Manure = 0.31',
            'Climate filename = climate.csv',
            'Climate Data Acquisition = nasa',
            'Use climate parameter instead of management factor = True',
            'Enable Carbon Modelling = True',
            '',
            '# Precipitation Data (mm)',
            'January Precipitation = 0',
            'February Precipitation = 1',
            'March Precipitation = 2',
            'April Precipitation = 3',
            'May Precipitation = 4',
            'June Precipitation = 5',
            'July Precipitation = 6',
            'August Precipitation = 7',
            'September Precipitation = 8',
            'October Precipitation = 9',
            'November Precipitation = 10',
            'December Precipitation = 11',
            '',
            '# Evapotranspiration Data (mm year^-1)',
            'January Potential Evapotranspiration = 0',
            'February Potential Evapotranspiration = 1',
            'March Potential Evapotranspiration = 2',
            'April Potential Evapotranspiration = 3',
            'May Potential Evapotranspiration = 4',
            'June Potential Evapotranspiration = 5',
            'July Potential Evapotranspiration = 6',
            'August Potential Evapotranspiration = 7',
            'September Potential Evapotranspiration = 8',
            'October Potential Evapotranspiration = 9',
            'November Potential Evapotranspiration = 10',
            'December Potential Evapotranspiration = 11',
            '',
            '# Temperature Data (°C)',
            'January Mean Temperature = 0',
            'February Mean Temperature = 1',
            'March Mean Temperature = 2',
            'April Mean Temperature = 3',
            'May Mean Temperature = 4',
            'June Mean Temperature = 5',
            'July Mean Temperature = 6',
            'August Mean Temperature = 7',
            'September Mean Temperature = 8',
            'October Mean Temperature = 9',
            'November Mean Temperature = 10',
            'December Mean Temperature = 11',
            '',
            '# Soil Data',
            'Province = toto',
            'Year Of Observation = 1',
            'Ecodistrict ID = 1',
            'Soil Great Group = toto',
            'Soil functional category = toto',
            'Bulk Density = 1.0',
            'Soil Texture = toto',
            'Soil Ph = 1.0',
            'Top Layer Thickness  (mm) = 1',
            'Proportion Of Sand In Soil = 1',
            'Proportion Of Clay In Soil = 1',
            'Proportion Of Soil Organic Carbon = 1'
        ]
        with self.path_farm_settings.open(mode='r', encoding='utf-8') as f:
            output = f.readlines()
        self.assertEqual(expected_output, [s.replace('\n', '') for s in output])
        pass


if __name__ == '__main__':
    unittest.main()
