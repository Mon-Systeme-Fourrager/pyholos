from holos_service.django_stuff import CanadianProvince
from holos_service.farm import farm_inputs
from holos_service.soil import SoilTexture

WEATHER_SUMMARY = farm_inputs.WeatherSummary(
    year=2024,
    mean_annual_precipitation=542,
    mean_annual_temperature=3.57,
    mean_annual_evapotranspiration=626,
    growing_season_precipitation=411,
    growing_season_evapotranspiration=573)

PROVINCE = CanadianProvince.Manitoba
SOIL_TEXTURE = SoilTexture.Fine
