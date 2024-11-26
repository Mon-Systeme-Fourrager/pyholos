from pathlib import Path

from geojson import load, FeatureCollection
from pandas import read_csv, DataFrame
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


def get_dominant_component_soil_id(
        id_polygon: int,
        path_slc_cmp: Path
) -> str:
    df = read_csv(path_slc_cmp, decimal='.', sep=',', usecols=['POLY_ID', 'PERCENT_', 'SOIL_ID'])
    return df[df['POLY_ID'] == id_polygon].sort_values(by='PERCENT_', ascending=False).iloc[0]['SOIL_ID']


def get_soil_layer_table(
        path_slc_slt: Path,
        id_soil: str
) -> DataFrame:
    df = read_csv(path_slc_slt, decimal='.', sep=',', usecols=["SOIL_ID", "UDEPTH", "LDEPTH"])
    df = df[df['SOIL_ID'] == id_soil]
    return df.sort_values(by='UDEPTH', ascending=True)


def get_first_non_litter_layer(
        soil_layer_table: DataFrame
) -> dict:
    return soil_layer_table[soil_layer_table['UDEPTH'] >= 0].iloc[0].to_dict()


def get_top_layer_depth(
        first_non_litter_layer: dict
) -> int:
    """

    Args:
        first_non_litter_layer: first soil layer which is not a litter

    Returns:
        (mm) depth of the upper first non-litter layer

    """
    return first_non_litter_layer['LDEPTH'] * 10
