import unittest
from pathlib import Path

from geojson import load

from holos_service import django_stuff

class TestIdentifySlcPolygonId(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        path_geojson = Path(__file__).parent / 'sources/geojson_example/example.geojson'
        with path_geojson.open(mode='r') as f:
            cls.geojson_data = load(f)
        django_stuff.PATH_SLC_GEOJSON_FILE = path_geojson

    def test_identify_slc_polygon_id_works_with_default_slc_data(self):
        self.assertEqual(
            851003,
            django_stuff.identify_slc_polygon_id(
                latitude=49.98,
                longitude=-98.04))

    def test_identify_slc_polygon_id_returns_expected_result(self):
        self.assertEqual(
            851003,
            django_stuff.identify_slc_polygon_id(
                latitude=49.98,
                longitude=-98.04,
                geojson_data=self.geojson_data))

        self.assertEqual(
            851003,
            django_stuff.identify_slc_polygon_id(
                latitude="49.98",
                longitude="-98.04",
                geojson_data=self.geojson_data))

    def test_identify_slc_polygon_id_fails_with_missing_location_data(self):
        self.assertRaises(
            TypeError,
            django_stuff.identify_slc_polygon_id,
            dict(longitude=-98.04, geojson_data=self.geojson_data))


if __name__ == '__main__':
    unittest.main()
