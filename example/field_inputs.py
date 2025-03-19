from holos_service.components.animals.common import ManureAnimalSourceTypes, ManureStateType, ManureLocationSourceType
from holos_service.components.land_management.common import (
    TillageType, IrrigationType, HarvestMethod, FertilizerBlends, ManureApplicationTypes)
from holos_service.components.land_management.crop import CropType
from holos_service.farm.farm_inputs import FieldsInput, FieldAnnualData, WeatherData


def set_field_data(weather_data: WeatherData) -> FieldsInput:
    field_annual_data = FieldAnnualData(
        name='field_1',
        field_area=1,
        weather_data=weather_data,
        crop_type=CropType.Wheat,
        crop_yield=2700,
        crop_year=2024,
        under_sown_crops_used=False,
        tillage_type=TillageType.Reduced,
        harvest_method=HarvestMethod.CashCrop,
        nitrogen_fertilizer_rate=100,
        fertilizer_blend=FertilizerBlends.Custom,
        irrigation_type=IrrigationType.Irrigated,
        amount_of_irrigation=0,
        number_of_pesticide_passes=0,
        amount_of_manure_applied=0,
        manure_application_type=ManureApplicationTypes.NotSelected,
        manure_animal_source_type=ManureAnimalSourceTypes.NotSelected,
        manure_state_type=ManureStateType.not_selected,
        manure_location_source_type=ManureLocationSourceType.NotSelected
    )
    return FieldsInput(
        fields=dict(
            field_1=[field_annual_data]
        )
    )
