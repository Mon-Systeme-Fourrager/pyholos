from holos_service.components.common import convert_province_name
from holos_service.components.land_management.common import IrrigationType
from holos_service.components.land_management.crop import CropType, convert_crop_type_name
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
