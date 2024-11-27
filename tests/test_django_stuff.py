import unittest
from pathlib import Path

from geojson import load

from holos_service import django_stuff


class TestGetSlcPolygonProperties(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        path_geojson = Path(__file__).parent / (
            'sources/django_stuff/example_soil_landscapes_of_canada_v3r2/soil_landscapes_of_canada_v3r2.geojson')
        with path_geojson.open(mode='r') as f:
            cls.geojson_data = load(f)
        django_stuff.PATH_SLC_GEOJSON_FILE = path_geojson
        cls.expected_outputs = {
            'OBJECTID': 9139,
            'AREA': 0.06119253235,
            'PERIMETER': 2.0076591166,
            'POLY_ID': 851003,
            'ECO_ID': 851,
            'Shape_Length': 2.0076591152263235,
            'Shape_Area': 0.06119253234576638}

    def test_identify_slc_polygon_id_works_with_default_slc_data(self):
        self.assertEqual(
            self.expected_outputs,
            django_stuff.get_slc_polygon_properties(
                latitude=49.98,
                longitude=-98.04))

    def test_identify_slc_polygon_id_returns_expected_result(self):
        self.assertEqual(
            self.expected_outputs,
            django_stuff.get_slc_polygon_properties(
                latitude=49.98,
                longitude=-98.04,
                geojson_data=self.geojson_data))

        self.assertEqual(
            self.expected_outputs,
            django_stuff.get_slc_polygon_properties(
                latitude="49.98",
                longitude="-98.04",
                geojson_data=self.geojson_data))

    def test_identify_slc_polygon_id_fails_with_missing_location_data(self):
        self.assertRaises(
            TypeError,
            django_stuff.get_slc_polygon_properties,
            dict(longitude=-98.04, geojson_data=self.geojson_data))


if __name__ == '__main__':
    unittest.main()
