from pathlib import Path

from geojson import load, FeatureCollection
from pandas import read_csv, DataFrame
from shapely.geometry import shape, Point

from holos_service.config import PathsSlcData


class MapProvinceNamesSlc(Enum):
    AB: int = 'Alberta'
    BC: int = 'British Columbia'
    MB: int = 'Manitoba'
    NB: int = 'New Brunswick'
    NL: int = 'Newfoundland and Labrador'
    NT: int = 'Northwest Territories'
    NS: int = 'Nova Scotia'
    NU: int = 'Nunavut'
    ON: int = 'Ontario'
    PE: int = 'Prince Edward Island'
    QC: int = 'Quebec'
    SK: int = 'Saskatchewan'
    YT: int = 'Yukon'

    @classmethod
    def get_value(cls, province_abbreviation: str) -> str:
        return getattr(cls, province_abbreviation).value


class MapSoilGreatGroupNamesSlc(Enum):
    MB: int = 'Melanic Brunisol'
    EB: int = 'Eutric Brunisol'
    SB: int = 'Sombric Brunisol'
    DYB: int = 'Dystric Brunisol'
    BC: int = 'Brown Chernozem'
    DBC: int = 'Dark Brown Chernozem'
    BLC: int = 'Black Chernozem'
    DGC: int = 'Dark Gray Chernozem'
    TC: int = 'Turbic Cryosol'
    SC: int = 'Static Cryosol'
    OC: int = 'Organic Cryosol'
    HG: int = 'Humic Gleysol'
    G: int = 'Gleysol'
    LG: int = 'Luvic Gleysol'
    GBL: int = 'Gray Brown Luvisol'
    GL: int = 'Gray Luvisol'
    F: int = 'Fibrisol'
    M: int = 'Mesisol'
    H: int = 'Humisol'
    FO: int = 'Folisol'
    HP: int = 'Humic Podzol'
    FHP: int = 'Ferro-Humic Podzol'
    HFP: int = 'Humo-Ferric Podzol'
    R: int = 'Regosol'
    HR: int = 'Humic Regosol'
    SZ: int = 'Solonetz'
    SS: int = 'Solodized Solonetz'
    SO: int = 'Solod'
    VSZ: int = 'Vertic Solonetz'
    V: int = 'Vertisol'
    HV: int = 'Humic Vertisol'

    @classmethod
    def get_value(cls, province_abbreviation: str) -> str:
        return getattr(cls, province_abbreviation).value


class MapParentMaterialTextureNamesSlc(Enum):
    VC: int = 'Very Coarse'
    C: int = 'Coarse'
    MC: int = 'Moderately Coarse'
    M: int = 'Medium'
    MF: int = 'Moderately Fine'
    F: int = 'Fine'
    VF: int = 'Very Fine'
    CS: int = 'Coarse Skeletal'
    MS: int = 'Medium Skeletal'
    FS: int = 'Fine Skeletal'
    FR: int = 'Fragmental'
    SM: int = 'Stratified (Mineral)'
    SU: int = 'Stratified (Mineral and Organic)'
    FI: int = 'Fibric'
    ME: int = 'Mesic'
    HU: int = 'Humic'
    UD: int = 'Undifferentiated'

    @classmethod
    def get_value(cls, province_abbreviation: str) -> str:
        return getattr(cls, province_abbreviation).value



    @classmethod
    def get_value(cls, province_abbreviation: str) -> str:
        return getattr(cls, province_abbreviation).value


def read_slc_csv(
        path_file: Path,
        **kwargs
) -> DataFrame:
    return read_csv(path_file, sep=',', decimal='.', **kwargs)


def load_slc_data(path_slc_geojson_file: Path) -> FeatureCollection:
    with path_slc_geojson_file.open(mode='r') as f:
        return load(f)


def get_slc_polygon_properties(
        latitude: float | str,
        longitude: float | str,
        geojson_data: FeatureCollection = None
) -> dict | None:
    if geojson_data is None:
        geojson_data = load_slc_data(path_slc_geojson_file=PathsSlcData.geojson_file.value)

    point = Point(longitude, latitude)

    for feature in geojson_data['features']:
        polygon = shape(feature['geometry'])
        if polygon.contains(point):
            return feature['properties']

    return None


def get_dominant_component_properties(
        id_polygon: int,
        slc_components_table: DataFrame
) -> dict[str, str | int]:
    return slc_components_table[slc_components_table['POLY_ID'] == id_polygon].sort_values(
        by='PERCENT_', ascending=False).iloc[0].to_dict()


def get_soil_layer_table(
        id_soil: str,
        slc_soil_layer_table: DataFrame
) -> DataFrame:
    return slc_soil_layer_table[slc_soil_layer_table['SOIL_ID'] == id_soil].sort_values(by='UDEPTH', ascending=True)


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
