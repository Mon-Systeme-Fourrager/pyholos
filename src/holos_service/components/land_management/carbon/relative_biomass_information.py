from holos_service.components.common import convert_province_name
from holos_service.components.land_management.common import IrrigationType
from holos_service.components.land_management.crop import CropType, convert_crop_type_name
from holos_service.config import PathsHolosResources
from holos_service.django_stuff import CanadianProvince


class _IrrigationData:
    def __init__(
            self,
            irrigation_type: IrrigationType,
            irrigation_lower_range_limit: float,
            irrigation_upper_range_limit: float
    ):
        self.irrigation_type = irrigation_type
        self.irrigation_lower_range_limit = irrigation_lower_range_limit
        self.irrigation_upper_range_limit = irrigation_upper_range_limit


class _CarbonResidueData:
    def __init__(
            self,
            relative_biomass_product: float,
            relative_biomass_straw: float,
            relative_biomass_root: float,
            relative_biomass_extraroot: float
    ):
        self.relative_biomass_product = relative_biomass_product
        self.relative_biomass_straw = relative_biomass_straw
        self.relative_biomass_root = relative_biomass_root
        self.relative_biomass_extraroot = relative_biomass_extraroot


class _NitrogenResidueData:
    def __init__(
            self,
            nitrogen_content_product: float,
            nitrogen_content_straw: float,
            nitrogen_content_root: float
    ):
        self.nitrogen_content_product = nitrogen_content_product
        self.nitrogen_content_straw = nitrogen_content_straw
        self.nitrogen_content_root = nitrogen_content_root
        self.nitrogen_content_extraroot = nitrogen_content_root


class BiogasAndMethaneProductionParametersData:
    def __init__(
            self,
            crop_type: CropType,
            bio_methane_potential,
            methane_fraction,
            volatile_solids,
            total_solids,
            total_nitrogen
    ):
        """Table_46_Biogas_Methane_Production_CropResidue_Data

        Args:
            crop_type: CropType class member
            bio_methane_potential: (Nm3 ton-1 VS) Biomethane potential given a subtrate type (BMP)
            methane_fraction: (-) fraction of methane in biogas (f_CH4)
            volatile_solids: (%) percentage of total solids
            total_solids: (kg t^-1)^3 total solids in the substrate type (TS)
            total_nitrogen: (KG N t^-1)^5 total Nitrogen in the substrate
        """
        self.crop_type = crop_type
        self.bio_methane_potential = bio_methane_potential
        self.methane_fraction = methane_fraction
        self.volatile_solids = volatile_solids
        self.total_solids = total_solids
        self.total_nitrogen = total_nitrogen


def parse_crop_type(
        raw_input: str
) -> CropType:
    return convert_crop_type_name(name=raw_input)


def parse_irrigation_data(
        raw_input: str,
) -> _IrrigationData:
    raw_input = raw_input.replace(' ', '').lower()

    irrigation_type = IrrigationType.RainFed if raw_input == "rainfed" else (
        IrrigationType.Irrigated if raw_input == "irrigated" else None)

    if "<" in raw_input:
        # Lower range
        irrigation_lower_range_limit = 0
        irrigation_upper_range_limit = float(raw_input.replace("<", "").replace("mm", ""))

    elif ">" in raw_input:
        # Upper range
        irrigation_lower_range_limit = float(raw_input.replace(">", "").replace("mm", ""))
        irrigation_upper_range_limit = float('inf')

    elif "-" in raw_input:
        # Irrigation is a range
        irrigation_lower_range_limit, irrigation_upper_range_limit = [
            float(s) for s in raw_input.replace("mm", "").replace(" ", "").split('-')]
    else:
        irrigation_lower_range_limit = None
        irrigation_upper_range_limit = None

    return _IrrigationData(
        irrigation_type=irrigation_type,
        irrigation_lower_range_limit=irrigation_lower_range_limit,
        irrigation_upper_range_limit=irrigation_upper_range_limit)


def parse_province_data(
        raw_input: str
) -> None | CanadianProvince:
    raw_input = raw_input.lower().replace(' ', '')
    if any([len(raw_input) == 0] + [v in raw_input for v in ["canada", "rainfed", "irrigated", ">", "<", "-"]]):
        province = None
    else:
        province = convert_province_name(name=raw_input)

    return province


def parse_moisture_content_data(
        raw_input: str
) -> float:
    raw_input = raw_input.lower().replace(" ", "")
    return float(raw_input) if not len(raw_input) == 0 else None


def parse_carbon_residue_data(
        raw_inputs: list[str]
) -> _CarbonResidueData:
    raw_inputs = [float(s) if len(s.lower().replace(" ", "")) != 0 else None for s in raw_inputs]
    return _CarbonResidueData(
        relative_biomass_product=raw_inputs[0],
        relative_biomass_straw=raw_inputs[1],
        relative_biomass_root=raw_inputs[2],
        relative_biomass_extraroot=raw_inputs[3]
    )


def parse_nitrogen_residue_data(
        raw_inputs: list[str]
) -> _NitrogenResidueData:
    raw_inputs = [float(s) if len(s.lower().replace(" ", "")) != 0 else None for s in raw_inputs]
    return _NitrogenResidueData(
        nitrogen_content_product=raw_inputs[0],
        nitrogen_content_straw=raw_inputs[1],
        nitrogen_content_root=raw_inputs[2]
    )


def parse_lignin_content_data(
        raw_input: str
) -> float:
    return float(raw_input) if len(raw_input.lower().replace(" ", "")) != 0 else None


def parse_biomethane_data(
        crop_type: CropType,
        raw_inputs: list[str]
) -> BiogasAndMethaneProductionParametersData:
    raw_inputs = [float(s) if len(s.lower().replace(" ", "")) != 0 else None for s in raw_inputs]
    return BiogasAndMethaneProductionParametersData(
        crop_type=crop_type,
        bio_methane_potential=raw_inputs[0],
        methane_fraction=raw_inputs[1],
        volatile_solids=raw_inputs[2],
        total_solids=raw_inputs[3],
        total_nitrogen=raw_inputs[4])
