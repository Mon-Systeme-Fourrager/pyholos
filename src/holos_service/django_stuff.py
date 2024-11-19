from geojson import load, FeatureCollection
from shapely.geometry import shape, Point

from holos_service.config import PATH_SLC_GEOJSON_FILE


def load_slc_data() -> FeatureCollection:
    with PATH_SLC_GEOJSON_FILE.open(mode='r') as f:
        return load(f)


def identify_slc_polygon_id(
        latitude: float | str,
        longitude: float | str,
        geojson_data: FeatureCollection = None
) -> int | None:
    if geojson_data is None:
        geojson_data = load_slc_data()

    point = Point(longitude, latitude)

    for feature in geojson_data['features']:
        polygon = shape(feature['geometry'])
        if polygon.contains(point):
            return feature['properties']['POLY_ID']

    return None
