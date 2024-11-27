from holos_service import django_stuff
from holos_service.config import PathsSlcData


def set_soil_texture_according_to_holos(
        soil_texture_abbreviation_from_slc: str
) -> str:
    soil_name = django_stuff.MapParentMaterialTextureNamesSlc.get_value(name=soil_texture_abbreviation_from_slc)
    if soil_name in ('Very Coarse', 'Coarse', 'Moderately Coarse'):
        res = 'Coarse'
    elif soil_name in ('Medium', 'Medium Skeletal'):
        res = 'Medium'
    elif soil_name in ('Moderately Fine', 'Fine', 'Very Fine', 'Fine Skeletal'):
        res = 'Fine'
    else:
        res = 'Medium'
    return res


def set_soil_properties(
        latitude: float,
        longitude: float,
        year_of_observation: int
) -> dict:
    polygon_properties = django_stuff.get_slc_polygon_properties(
        latitude=latitude,
        longitude=longitude,
        geojson_data=django_stuff.load_slc_data(
            path_slc_geojson_file=PathsSlcData.geojson_file.value))
    dominant_component_properties = django_stuff.get_dominant_component_properties(
        id_polygon=polygon_properties['POLY_ID'],
        slc_components_table=django_stuff.read_slc_csv(
            path_file=PathsSlcData.cmp_file.value,
            usecols=['POLY_ID', 'PROVINCE', 'PERCENT_', 'SOIL_ID']))
    id_soil = dominant_component_properties['SOIL_ID']
    soil_layer_table = django_stuff.get_soil_layer_table(
        id_soil=id_soil,
        slc_soil_layer_table=django_stuff.read_slc_csv(path_file=PathsSlcData.slt_file.value))
    first_non_litter_layer = django_stuff.get_first_non_litter_layer(
        soil_layer_table=soil_layer_table)
    soil_name_table = django_stuff.get_soil_name_table(
        soil_name_table=django_stuff.read_slc_csv(
            path_file=PathsSlcData.snt_file.value, usecols=['SOIL_ID', 'PMTEX1', 'G_GROUP3']),
        id_soil=id_soil)

    return {
        'Province': django_stuff.MapProvinceNamesSlc.get_value(dominant_component_properties['PROVINCE']),
        'Year Of Observation': year_of_observation,
        'Ecodistrict ID': polygon_properties['ECO_ID'],
        'Soil Great Group': django_stuff.MapSoilGreatGroupNamesSlc.get_value(
            soil_name_table['G_GROUP3']).replace(' ', ''),
        # Soil functional category = Black
        'Bulk Density': first_non_litter_layer['BD'],
        'Soil Texture': set_soil_texture_according_to_holos(
            soil_texture_abbreviation_from_slc=soil_name_table['PMTEX1']),
        'Soil Ph': round(first_non_litter_layer['PH2'], 1),
        'Top Layer Thickness  (mm)': first_non_litter_layer['LDEPTH'] * 10,
        'Proportion Of Sand In Soil': first_non_litter_layer['TSAND'] / 100.,
        'Proportion Of Clay In Soil': first_non_litter_layer['TCLAY'] / 100.,
        'Proportion Of Soil Organic Carbon': round(first_non_litter_layer['ORGCARB'], 2)
    }

    pass
