from holos_service import django_stuff
from holos_service.common import Region, get_region
from holos_service.config import PathsSlcData


class SoilFunctionalCategory:
    NotApplicable: str = "NotApplicable"
    Brown: str = "Brown"
    BrownChernozem: str = "BrownChernozem"
    DarkBrown: str = "DarkBrown"
    DarkBrownChernozem: str = "DarkBrownChernozem"
    Black: str = "Black"
    BlackGrayChernozem: str = "BlackGrayChernozem"
    Organic: str = "Organic"
    EasternCanada: str = "EasternCanada"
    # All: str = "EnumSoilFunctionalAll"
    Unknown: str = "Unknown"

    Grey: str = "Grey"
    DarkGrey: str = "DarkGrey"


class SoilGreatGroup:
    def __init__(
            self,
            soil_great_group_type: str,
            region: str,
            soil_functional_category: str
    ):
        self.soil_great_group_type = soil_great_group_type
        self.region = region
        self.soil_functional_category = soil_functional_category


def get_soil_great_group_table() -> list[SoilGreatGroup]:
    return [
        SoilGreatGroup(
            soil_great_group_type=django_stuff.SoilGreatGroupNamesSlc.BrownChernozem.name,
            region=Region.WesternCanada,
            soil_functional_category=SoilFunctionalCategory.Brown),
        SoilGreatGroup(
            soil_great_group_type=django_stuff.SoilGreatGroupNamesSlc.BrownChernozem.name,
            region=Region.EasternCanada,
            soil_functional_category=SoilFunctionalCategory.NotApplicable),
        SoilGreatGroup(
            soil_great_group_type=django_stuff.SoilGreatGroupNamesSlc.DarkBrownChernozem.name,
            region=Region.WesternCanada,
            soil_functional_category=SoilFunctionalCategory.DarkBrown),
        SoilGreatGroup(
            soil_great_group_type=django_stuff.SoilGreatGroupNamesSlc.DarkBrownChernozem.name,
            region=Region.EasternCanada,
            soil_functional_category=SoilFunctionalCategory.NotApplicable),
        SoilGreatGroup(
            soil_great_group_type=django_stuff.SoilGreatGroupNamesSlc.BlackChernozem.name,
            region=Region.WesternCanada,
            soil_functional_category=SoilFunctionalCategory.Black),
        SoilGreatGroup(
            soil_great_group_type=django_stuff.SoilGreatGroupNamesSlc.BlackChernozem.name,
            region=Region.EasternCanada,
            soil_functional_category=SoilFunctionalCategory.NotApplicable),
        SoilGreatGroup(
            soil_great_group_type=django_stuff.SoilGreatGroupNamesSlc.DarkGrayChernozem.name,
            region=Region.WesternCanada,
            soil_functional_category=SoilFunctionalCategory.Black),
        SoilGreatGroup(
            soil_great_group_type=django_stuff.SoilGreatGroupNamesSlc.DarkGrayChernozem.name,
            region=Region.EasternCanada,
            soil_functional_category=SoilFunctionalCategory.NotApplicable),
        SoilGreatGroup(
            soil_great_group_type=django_stuff.SoilGreatGroupNamesSlc.Solonetz.name,
            region=Region.WesternCanada,
            soil_functional_category=SoilFunctionalCategory.Brown),
        SoilGreatGroup(
            soil_great_group_type=django_stuff.SoilGreatGroupNamesSlc.Solonetz.name,
            region=Region.EasternCanada,
            soil_functional_category=SoilFunctionalCategory.EasternCanada),
        SoilGreatGroup(
            soil_great_group_type=django_stuff.SoilGreatGroupNamesSlc.SolodizedSolonetz.name,
            region=Region.WesternCanada,
            soil_functional_category=SoilFunctionalCategory.Brown),
        SoilGreatGroup(
            soil_great_group_type=django_stuff.SoilGreatGroupNamesSlc.SolodizedSolonetz.name,
            region=Region.EasternCanada,
            soil_functional_category=SoilFunctionalCategory.EasternCanada),
        SoilGreatGroup(
            soil_great_group_type=django_stuff.SoilGreatGroupNamesSlc.Solod.name,
            region=Region.WesternCanada,
            soil_functional_category=SoilFunctionalCategory.Brown),
        SoilGreatGroup(
            soil_great_group_type=django_stuff.SoilGreatGroupNamesSlc.Solod.name,
            region=Region.EasternCanada,
            soil_functional_category=SoilFunctionalCategory.EasternCanada),
        SoilGreatGroup(
            soil_great_group_type=django_stuff.SoilGreatGroupNamesSlc.VerticSolonetz.name,
            region=Region.WesternCanada,
            soil_functional_category=SoilFunctionalCategory.Brown),
        SoilGreatGroup(
            soil_great_group_type=django_stuff.SoilGreatGroupNamesSlc.VerticSolonetz.name,
            region=Region.EasternCanada,
            soil_functional_category=SoilFunctionalCategory.EasternCanada),
        SoilGreatGroup(
            soil_great_group_type=django_stuff.SoilGreatGroupNamesSlc.GrayBrownLuvisol.name,
            region=Region.WesternCanada,
            soil_functional_category=SoilFunctionalCategory.NotApplicable),
        SoilGreatGroup(
            soil_great_group_type=django_stuff.SoilGreatGroupNamesSlc.GrayBrownLuvisol.name,
            region=Region.EasternCanada,
            soil_functional_category=SoilFunctionalCategory.EasternCanada),
        SoilGreatGroup(
            soil_great_group_type=django_stuff.SoilGreatGroupNamesSlc.GrayLuvisol.name,
            region=Region.WesternCanada,
            soil_functional_category=SoilFunctionalCategory.Black),
        SoilGreatGroup(
            soil_great_group_type=django_stuff.SoilGreatGroupNamesSlc.GrayLuvisol.name,
            region=Region.EasternCanada,
            soil_functional_category=SoilFunctionalCategory.EasternCanada),
        SoilGreatGroup(
            soil_great_group_type=django_stuff.SoilGreatGroupNamesSlc.FerroHumicPodzol.name,
            region=Region.WesternCanada,
            soil_functional_category=SoilFunctionalCategory.Brown),
        SoilGreatGroup(
            soil_great_group_type=django_stuff.SoilGreatGroupNamesSlc.FerroHumicPodzol.name,
            region=Region.EasternCanada,
            soil_functional_category=SoilFunctionalCategory.EasternCanada),
        SoilGreatGroup(
            soil_great_group_type=django_stuff.SoilGreatGroupNamesSlc.HumicPodzol.name,
            region=Region.WesternCanada,
            soil_functional_category=SoilFunctionalCategory.Brown),
        SoilGreatGroup(
            soil_great_group_type=django_stuff.SoilGreatGroupNamesSlc.HumicPodzol.name,
            region=Region.EasternCanada,
            soil_functional_category=SoilFunctionalCategory.EasternCanada),
        SoilGreatGroup(
            soil_great_group_type=django_stuff.SoilGreatGroupNamesSlc.HumoFerricPodzol.name,
            region=Region.WesternCanada,
            soil_functional_category=SoilFunctionalCategory.Brown),
        SoilGreatGroup(
            soil_great_group_type=django_stuff.SoilGreatGroupNamesSlc.HumoFerricPodzol.name,
            region=Region.EasternCanada,
            soil_functional_category=SoilFunctionalCategory.EasternCanada),
        SoilGreatGroup(
            soil_great_group_type=django_stuff.SoilGreatGroupNamesSlc.MelanicBrunisol.name,
            region=Region.WesternCanada,
            soil_functional_category=SoilFunctionalCategory.Brown),
        SoilGreatGroup(
            soil_great_group_type=django_stuff.SoilGreatGroupNamesSlc.MelanicBrunisol.name,
            region=Region.EasternCanada,
            soil_functional_category=SoilFunctionalCategory.EasternCanada),
        SoilGreatGroup(
            soil_great_group_type=django_stuff.SoilGreatGroupNamesSlc.EutricBrunisol.name,
            region=Region.WesternCanada,
            soil_functional_category=SoilFunctionalCategory.Brown),
        SoilGreatGroup(
            soil_great_group_type=django_stuff.SoilGreatGroupNamesSlc.EutricBrunisol.name,
            region=Region.EasternCanada,
            soil_functional_category=SoilFunctionalCategory.EasternCanada),
        SoilGreatGroup(
            soil_great_group_type=django_stuff.SoilGreatGroupNamesSlc.SombricBrunisol.name,
            region=Region.WesternCanada,
            soil_functional_category=SoilFunctionalCategory.Brown),
        SoilGreatGroup(
            soil_great_group_type=django_stuff.SoilGreatGroupNamesSlc.SombricBrunisol.name,
            region=Region.EasternCanada,
            soil_functional_category=SoilFunctionalCategory.EasternCanada),
        SoilGreatGroup(
            soil_great_group_type=django_stuff.SoilGreatGroupNamesSlc.DystricBrunisol.name,
            region=Region.WesternCanada,
            soil_functional_category=SoilFunctionalCategory.Brown),
        SoilGreatGroup(
            soil_great_group_type=django_stuff.SoilGreatGroupNamesSlc.DystricBrunisol.name,
            region=Region.EasternCanada,
            soil_functional_category=SoilFunctionalCategory.EasternCanada),
        SoilGreatGroup(
            soil_great_group_type=django_stuff.SoilGreatGroupNamesSlc.HumicGleysol.name,
            region=Region.WesternCanada,
            soil_functional_category=SoilFunctionalCategory.Brown),
        SoilGreatGroup(
            soil_great_group_type=django_stuff.SoilGreatGroupNamesSlc.HumicGleysol.name,
            region=Region.EasternCanada,
            soil_functional_category=SoilFunctionalCategory.EasternCanada),
        SoilGreatGroup(
            soil_great_group_type=django_stuff.SoilGreatGroupNamesSlc.Gleysol.name,
            region=Region.WesternCanada,
            soil_functional_category=SoilFunctionalCategory.Brown),
        SoilGreatGroup(
            soil_great_group_type=django_stuff.SoilGreatGroupNamesSlc.Gleysol.name,
            region=Region.EasternCanada,
            soil_functional_category=SoilFunctionalCategory.EasternCanada),
        SoilGreatGroup(
            soil_great_group_type=django_stuff.SoilGreatGroupNamesSlc.LuvicGleysol.name,
            region=Region.WesternCanada,
            soil_functional_category=SoilFunctionalCategory.Black),
        SoilGreatGroup(
            soil_great_group_type=django_stuff.SoilGreatGroupNamesSlc.LuvicGleysol.name,
            region=Region.EasternCanada,
            soil_functional_category=SoilFunctionalCategory.EasternCanada),
        SoilGreatGroup(
            soil_great_group_type=django_stuff.SoilGreatGroupNamesSlc.Fibrisol.name,
            region=Region.WesternCanada,
            soil_functional_category=SoilFunctionalCategory.Organic),
        SoilGreatGroup(
            soil_great_group_type=django_stuff.SoilGreatGroupNamesSlc.Fibrisol.name,
            region=Region.EasternCanada,
            soil_functional_category=SoilFunctionalCategory.Organic),
        SoilGreatGroup(
            soil_great_group_type=django_stuff.SoilGreatGroupNamesSlc.Mesisol.name,
            region=Region.WesternCanada,
            soil_functional_category=SoilFunctionalCategory.Organic),
        SoilGreatGroup(
            soil_great_group_type=django_stuff.SoilGreatGroupNamesSlc.Mesisol.name,
            region=Region.EasternCanada,
            soil_functional_category=SoilFunctionalCategory.Organic),
        SoilGreatGroup(
            soil_great_group_type=django_stuff.SoilGreatGroupNamesSlc.OrganicCryosol.name,
            region=Region.WesternCanada,
            soil_functional_category=SoilFunctionalCategory.Organic),
        SoilGreatGroup(
            soil_great_group_type=django_stuff.SoilGreatGroupNamesSlc.OrganicCryosol.name,
            region=Region.EasternCanada,
            soil_functional_category=SoilFunctionalCategory.Organic),
        SoilGreatGroup(
            soil_great_group_type=django_stuff.SoilGreatGroupNamesSlc.NotApplicable.name,
            region=Region.WesternCanada,
            soil_functional_category=SoilFunctionalCategory.NotApplicable),
        SoilGreatGroup(
            soil_great_group_type=django_stuff.SoilGreatGroupNamesSlc.NotApplicable.name,
            region=Region.EasternCanada,
            soil_functional_category=SoilFunctionalCategory.NotApplicable),

        SoilGreatGroup(
            soil_great_group_type=django_stuff.SoilGreatGroupNamesSlc.Unknown.name,
            region=Region.EasternCanada,
            soil_functional_category=SoilFunctionalCategory.EasternCanada),
    ]


def seek_soil_functional_category(
        province: str,
        soil_great_group: str
) -> str:
    region = get_region(province=province)

    for v in get_soil_great_group_table():
        if all([v.soil_great_group_type == soil_great_group, v.region == region]):
            return v.soil_functional_category


def get_soil_functional_category(
        province: str,
        soil_great_group: str
) -> str:
    soil_functional_category = seek_soil_functional_category(
        province=province,
        soil_great_group=soil_great_group)
    return soil_functional_category if soil_functional_category is not None else SoilFunctionalCategory.Black


def set_soil_texture_according_to_holos(
        soil_texture_abbreviation_from_slc: str
) -> str:
    soil_name = django_stuff.ParentMaterialTextureNamesSlc.get_name(abbreviation=soil_texture_abbreviation_from_slc)
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
        longitude: float
) -> dict:
    """Calculates the soil properties required by Holos 4.0

    Args:
        latitude: (decimal degrees) latitude of the simulated site
        longitude: (decimal degrees) longitude of the simulated site

    Returns:
        The following key-value pairs:
            id_polygon (int): ID of the SLC polygon in which the site is located
            province (str): The Canadian Province in which the site is located
            ecodistrict_id (int): ID of the Ecodistrict within which the farm is located
            soil_great_group (str): soil great group (e.g. "Regosol")
            soil_functional_category (str): soil functional (e.g. "Black")
            bulk_density (float): (g cm-3) soil bulk density
            soil_texture (str): soil texture (e.g. "Fine")
            soil_ph (float): (-) soil pH
            top_layer_thickness (float): (mm) thickness of the soil top layer
            sand_proportion (float): (between 0 and 1) fraction of sand in soil
            clay_proportion (float): (between 0 and 1) fraction of clay in soil
            organic_carbon_proportion (float): (between 0 and 100) percentage of soil organic carbon in soil

    """
    polygon_properties = django_stuff.get_slc_polygon_properties(
        latitude=latitude,
        longitude=longitude,
        geojson_data=django_stuff.load_slc_data(
            path_slc_geojson_file=PathsSlcData.geojson_file.value))
    id_polygon = polygon_properties['POLY_ID']
    dominant_component_properties = django_stuff.get_dominant_component_properties(
        id_polygon=id_polygon,
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

    province = django_stuff.CanadianProvince.get_name(abbreviation=dominant_component_properties['PROVINCE'])
    soil_great_group = django_stuff.SoilGreatGroupNamesSlc.get_name(
        abbreviation=soil_name_table['G_GROUP3']).replace(' ', '')

    return dict(
        id_polygon=id_polygon,
        province=province,
        ecodistrict_id=polygon_properties['ECO_ID'],
        soil_great_group=soil_great_group,
        soil_functional_category=get_soil_functional_category(
            province=province,
            soil_great_group=soil_great_group),
        bulk_density=first_non_litter_layer['BD'],
        soil_texture=set_soil_texture_according_to_holos(
            soil_texture_abbreviation_from_slc=soil_name_table['PMTEX1']),
        soil_ph=round(first_non_litter_layer['PH2'], 1),
        top_layer_thickness=first_non_litter_layer['LDEPTH'] * 10,
        sand_proportion=first_non_litter_layer['TSAND'] / 100.,
        clay_proportion=first_non_litter_layer['TCLAY'] / 100.,
        organic_carbon_proportion=round(first_non_litter_layer['ORGCARB'], 2))

    pass
