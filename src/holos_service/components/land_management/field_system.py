from uuid import UUID

from holos_service.common import HolosVar, Component
from holos_service.components.animals.common import ManureAnimalSourceTypes, ManureStateType, ManureLocationSourceType
from holos_service.components.land_management.carbon.climate import calculate_climate_parameter
from holos_service.components.land_management.carbon.management import calculate_management_factor
from holos_service.components.land_management.carbon.relative_biomass_information import (
    RelativeBiomassInformationData, get_nitrogen_lignin_content_in_crops_data, parse_table_9)
from holos_service.components.land_management.carbon.tillage import calculate_tillage_factor
from holos_service.components.land_management.common import (
    TillageType, HarvestMethod, IrrigationType, ManureApplicationTypes, TimePeriodCategory, get_fuel_energy_estimate,
    get_herbicide_energy_estimate, FertilizerBlends)
from holos_service.components.land_management.crop import get_nitrogen_fixation, CropType
from holos_service.core_constants import CoreConstants
from holos_service.defaults import Defaults
from holos_service.django_stuff import CanadianProvince
from holos_service.soil import SoilFunctionalCategory

TABLE_9 = parse_table_9()


class LandManagementBase(Component):
    def __init__(self):
        super().__init__()
        self.phase_number = HolosVar(name='Phase Number', value=0)
        """deprecated"""

        self.name = HolosVar(name='Name')
        self.area = HolosVar(name='Area')
        self.current_year = HolosVar(name='Current Year')
        self.crop_year = HolosVar(name='Crop Year')
        self.crop_type = HolosVar(name='Crop Type')
        self.tillage_type = HolosVar(name='Tillage Type')
        self.year_in_perennial_stand = HolosVar(name='Year In Perennial Stand')
        self.perennial_stand_id = HolosVar(name='Perennial Stand ID')
        self.perennial_stand_length = HolosVar(name='Perennial Stand Length')
        self.biomass_coefficient_product = HolosVar(name='Biomass Coefficient Product')
        self.biomass_coefficient_straw = HolosVar(name='Biomass Coefficient Straw')
        self.biomass_coefficient_roots = HolosVar(name='Biomass Coefficient Roots')
        self.biomass_coefficient_extraroot = HolosVar(name='Biomass Coefficient Extraroot')
        self.nitrogen_content_in_product = HolosVar(name='Nitrogen Content In Product')
        self.nitrogen_content_in_straw = HolosVar(name='Nitrogen Content In Straw')
        self.nitrogen_content_in_roots = HolosVar(name='Nitrogen Content In Roots')
        self.nitrogen_content_in_extraroot = HolosVar(name='Nitrogen Content In Extraroot')
        self.nitrogen_fixation = HolosVar(name='Nitrogen Fixation')

        self.nitrogen_deposit = HolosVar(name='Nitrogen Deposit', value=CoreConstants.NitrogenDepositionAmount)
        """(kg(N) ha-1 year-1) Atmospheric Nitrogen deposition amount"""

        self.carbon_concentration = HolosVar(name='Carbon Concentration', value=CoreConstants.CarbonConcentration)
        """(kg(C)/kg(plant biomass)) carbon concentration in plant biomass"""

        self.crop_yield = HolosVar(name='Yield')
        self.harvest_method = HolosVar(name='Harvest Method')
        self.nitrogen_fertilizer_rate = HolosVar(name='Nitrogen Fertilizer Rate')

        self.phosphorous_fertilizer_rate = HolosVar(name='Phosphorous Fertilizer Rate', value=0)
        """Not used/implemented yet in Holos v.4. Future version will utilize"""

        self.is_irrigated = HolosVar(name='Is Irrigated', value="No")
        """Not used/implemented yet in Holos v.4. Future version will utilize"""

        self.irrigation_type = HolosVar(name='Irrigation Type')
        self.amount_of_irrigation = HolosVar(name='Amount Of Irrigation')
        self.moisture_content_of_crop = HolosVar(name='Moisture Content Of Crop')
        self.moisture_content_of_crop_percentage = HolosVar(name='Moisture Content Of Crop Percentage')
        self.percentage_of_straw_returned_to_soil = HolosVar(name='PercentageOfStrawReturnedToSoil')
        self.percentage_of_roots_returned_to_soil = HolosVar(name='PercentageOfRootsReturnedToSoil')
        self.percentage_of_product_yield_returned_to_soil = HolosVar(name='PercentageOfProductYieldReturnedToSoil')
        self.is_pesticide_used = HolosVar(name='Is Pesticide Used')
        self.number_of_pesticide_passes = HolosVar(name='Number Of Pesticide Passes')
        self.manure_applied = HolosVar(name='Manure Applied')
        self.amount_of_manure_applied = HolosVar(name='Amount Of Manure Applied')
        self.manure_application_type = HolosVar(name='Manure Application Type')
        self.manure_animal_source_type = HolosVar(name='Manure Animal Source Type')
        self.manure_state_type = HolosVar(name='Manure State Type')
        self.manure_location_source_type = HolosVar(name='Manure Location Source Type')
        self.under_sown_crops_used = HolosVar(name='Under Sown Crops Used')

        self.crop_is_grazed = HolosVar(name='Crop Is Grazed', value="False")
        """Not used/implemented yet in Holos v.4. Future version will utilize"""

        self.field_system_component_guid = HolosVar(name='Field System Component Guid')

        self.time_period_category = HolosVar(name='Time Period Category String', value=TimePeriodCategory.Current)
        """Used to indicate time period in field history. Leave as "Current" if not sure"""

        self.climate_parameter = HolosVar(name='Climate Parameter')
        self.tillage_factor = HolosVar(name='Tillage Factor')
        self.management_factor = HolosVar(name='Management Factor')

        self.plant_carbon_in_agricultural_product = HolosVar(name='Plant Carbon In Agricultural Product', value=0)
        """deprecated"""

        self.carbon_input_from_product = HolosVar(name='Carbon Input From Product', value=0)
        """deprecated"""

        self.carbon_input_from_straw = HolosVar(name='Carbon Input From Straw', value=0)
        """deprecated"""

        self.carbon_input_from_roots = HolosVar(name='Carbon Input From Roots', value=0)
        """deprecated"""

        self.carbon_input_from_extraroots = HolosVar(name='Carbon Input From Extraroots', value=0)
        """deprecated"""

        self.size_of_first_rotation_for_field = HolosVar(name='Size Of First Rotation For Field', value=1)
        """deprecated"""

        self.above_ground_carbon_input = HolosVar(name='Above Ground Carbon Input', value=0)
        """deprecated"""

        self.below_ground_carbon_input = HolosVar(name='Below Ground Carbon Input', value=0)
        """deprecated"""

        self.manure_carbon_inputs_per_hectare = HolosVar(name='Manure Carbon Inputs Per Hectare', value=0)
        """deprecated"""

        self.digestate_carbon_inputs_per_hectare = HolosVar(name='Digestate Carbon Inputs Per Hectare', value=0)
        """deprecated"""

        self.total_carbon_inputs = HolosVar(name='Total Carbon Inputs', value=0)
        """deprecated"""

        self.sand = HolosVar(name='Sand')
        """(-) fraction of sand in soil (between 0 and 1)"""

        self.lignin = HolosVar(name='Lignin')
        """(-) fraction of lignin content in the carbon input (on dry basis, between 0 and 1)"""

        self.w_fac = HolosVar(name='WFac', value=0)
        """deprecated"""

        self.t_fac = HolosVar(name='TFac', value=0)
        """deprecated"""

        self.total_nitrogen_inputs_for_ipcc_tier2 = HolosVar(name='Total Nitrogen Inputs For Ipcc Tier 2', value=0)
        """deprecated"""

        self.nitrogen_content = HolosVar(name='Nitrogen Content')
        """(-) Nitrogen fraction of the carbon input (from IPCC Tier 2, between 0 and 1)"""

        self.above_ground_residue_dry_matter = HolosVar(name='Above Ground Residue Dry Matter', value=0)
        """deprecated"""

        self.below_ground_residue_dry_matter = HolosVar(name='Below Ground Residue Dry Matter', value=0)
        """deprecated"""

        self.fuel_energy = HolosVar(name='Fuel Energy')
        self.herbicide_energy = HolosVar(name='Herbicide Energy')
        self.fertilizer_blend = HolosVar(name='Fertilizer Blend')

    def get_default_harvest_method(self) -> HarvestMethod:
        """Returns default harvest method based on the cultivated crop.

        Returns:
            HarvestMethod class member

        Holos source code:
            https://github.com/holos-aafc/Holos/blob/b183dab99d211158d1fed9da5370ce599ac7c914/H.Core/Services/Initialization/Crops/CropInitializationService.Harvest.cs#L19
        """
        return HarvestMethod.Silage if self.crop_type.value.is_silage_crop() else HarvestMethod.CashCrop

    def set_irrigation_type(self):
        """Sets the irrigation type, irrigated or rainfed, based on the presence or absence of irrigation amount, resp.

        Holos source code:
            https://github.com/holos-aafc/Holos/blob/23a53f1fe6796145cc3ac43c005dbcc560421deb/H.Core/Models/LandManagement/Fields/CropViewItem.cs#L1289
        """
        self.irrigation_type.value = IrrigationType.Irrigated if self.amount_of_irrigation.value > 0 else IrrigationType.RainFed

    def set_moisture_content(self):
        if any([
            self.harvest_method == HarvestMethod.GreenManure,
            self.harvest_method == HarvestMethod.Silage,
            self.harvest_method == HarvestMethod.Swathing,
            self.crop_type.value.is_silage_crop()
        ]):
            """Sets the moisture percentage of the harvested biomass.
            
            Holos source code:
                https://github.com/holos-aafc/Holos/blob/23a53f1fe6796145cc3ac43c005dbcc560421deb/H.Core/Services/Initialization/Crops/CropInitializationService.Water.cs#L60
            """
            moisture_content_of_crop_percentage = 65

        else:
            if self.moisture_content_of_crop.value != 0:
                moisture_content_of_crop_percentage = self.moisture_content_of_crop.value * 100.
            else:
                moisture_content_of_crop_percentage = 12

        self.moisture_content_of_crop_percentage.value = moisture_content_of_crop_percentage

    def set_percentage_returns(self):
        """
        Holos source code:
            https://github.com/holos-aafc/Holos/blob/bf38e27113cd965442cafb118f7ce156c8065701/H.Core/Services/Initialization/Crops/CropInitializationService.Returns.cs#L24
        """
        percentage_of_product_yield_returned_to_soil = 0
        percentage_of_straw_returned_to_soil = 0
        percentage_of_roots_returned_to_soil = 0

        # Initialize the view item by checking the crop type
        crop_type: CropType = self.crop_type.value
        if crop_type.is_perennial():
            percentage_of_product_yield_returned_to_soil = Defaults.PercentageOfProductReturnedToSoilForPerennials
            percentage_of_straw_returned_to_soil = 0
            percentage_of_roots_returned_to_soil = Defaults.PercentageOfRootsReturnedToSoilForPerennials
        elif crop_type.is_annual():
            percentage_of_product_yield_returned_to_soil = Defaults.PercentageOfProductReturnedToSoilForAnnuals
            percentage_of_straw_returned_to_soil = Defaults.PercentageOfStrawReturnedToSoilForAnnuals
            percentage_of_roots_returned_to_soil = Defaults.PercentageOfRootsReturnedToSoilForAnnuals

        if crop_type.is_root_crop():
            percentage_of_product_yield_returned_to_soil = Defaults.PercentageOfProductReturnedToSoilForRootCrops
            percentage_of_straw_returned_to_soil = Defaults.PercentageOfStrawReturnedToSoilForRootCrops

        if crop_type.is_cover_crop():
            percentage_of_product_yield_returned_to_soil = 100
            percentage_of_straw_returned_to_soil = 100
            percentage_of_roots_returned_to_soil = 100

        # Initialize the view item by checking the harvest method (override any setting based on crop type)
        harvest_method = self.harvest_method.value
        if any([
            crop_type.is_silage_crop(),
            harvest_method == HarvestMethod.Silage
        ]):
            percentage_of_product_yield_returned_to_soil = 2
            percentage_of_straw_returned_to_soil = 0
            percentage_of_roots_returned_to_soil = 100
        elif harvest_method == HarvestMethod.Swathing:
            percentage_of_product_yield_returned_to_soil = 30
            percentage_of_straw_returned_to_soil = 0
            percentage_of_roots_returned_to_soil = 100
        elif harvest_method == HarvestMethod.GreenManure:
            percentage_of_product_yield_returned_to_soil = 100
            percentage_of_straw_returned_to_soil = 0
            percentage_of_roots_returned_to_soil = 100

        self.percentage_of_product_yield_returned_to_soil.value = percentage_of_product_yield_returned_to_soil
        self.percentage_of_straw_returned_to_soil.value = percentage_of_straw_returned_to_soil
        self.percentage_of_roots_returned_to_soil.value = percentage_of_roots_returned_to_soil

        pass

    def initialize_biomass_coefficients(
            self,
            residue_data: RelativeBiomassInformationData
    ):
        self.biomass_coefficient_product.value = residue_data.RelativeBiomassProduct
        self.biomass_coefficient_straw.value = residue_data.RelativeBiomassStraw
        self.biomass_coefficient_roots.value = residue_data.RelativeBiomassRoot
        self.biomass_coefficient_extraroot.value = residue_data.RelativeBiomassExtraroot

        if self.harvest_method.value in [
            HarvestMethod.Swathing,
            HarvestMethod.GreenManure,
            HarvestMethod.Silage
        ]:
            self.biomass_coefficient_product.value = residue_data.RelativeBiomassProduct + residue_data.RelativeBiomassStraw
            self.biomass_coefficient_straw.value = 0
            self.biomass_coefficient_roots.value = residue_data.RelativeBiomassRoot
            self.biomass_coefficient_extraroot.value = residue_data.RelativeBiomassExtraroot

    def initialize_nitrogen_content(
            self,
            residue_data: RelativeBiomassInformationData
    ):
        """

        Args:
            residue_data: RelativeBiomassInformationData instance

        Holos source code:
            https://github.com/holos-aafc/Holos/blob/71638efd97c84c6ded45e342ce664477df6f803f/H.Core/Services/Initialization/Crops/CropInitializationService.Nitrogen.cs#L42
        """
        # Assign N content values used for the ICBM methodology

        # Table has values in grams but unit of display is kg
        self.nitrogen_content_in_product.value = residue_data.NitrogenContentProduct / 1000
        self.nitrogen_content_in_straw.value = residue_data.NitrogenContentStraw / 1000
        self.nitrogen_content_in_roots.value = residue_data.NitrogenContentRoot / 1000
        self.nitrogen_content_in_extraroot.value = residue_data.NitrogenContentExtraroot / 1000

        if self.crop_type.value.is_perennial():
            self.nitrogen_content_in_straw.value = 0

        # Assign N content values used for IPCC Tier 2
        crop_data = get_nitrogen_lignin_content_in_crops_data(
            crop_type=self.crop_type.value,
            table_9=TABLE_9)

        self.nitrogen_content.value = crop_data.NitrogenContentResidues


class CropViewItem(LandManagementBase):
    def __init__(
            self,
            name: str,
            field_area: float,
            current_year: int,
            crop_year: int,
            year_in_perennial_stand: int,
            crop_type: CropType,
            tillage_type: TillageType,
            perennial_stand_id: UUID,
            perennial_stand_length: int,
            relative_biomass_information_data: RelativeBiomassInformationData,
            crop_yield: float,
            harvest_method: HarvestMethod,
            nitrogen_fertilizer_rate: float,
            under_sown_crops_used: bool,
            field_system_component_guid: UUID,
            province: CanadianProvince,
            clay_content: float,
            sand_content: float,
            organic_carbon_percentage: float,
            soil_top_layer_thickness: float,
            soil_functional_category: SoilFunctionalCategory,
            fertilizer_blend: FertilizerBlends,
            evapotranspiration: list[float],
            precipitation: list[float],
            temperature: list[float],

            amount_of_irrigation: float = 0,
            number_of_pesticide_passes: int = 0,
            amount_of_manure_applied: float = 0,
            manure_application_type: ManureApplicationTypes = ManureApplicationTypes.NotSelected,
            manure_animal_source_type: ManureAnimalSourceTypes = ManureAnimalSourceTypes.NotSelected,
            manure_state_type: ManureStateType = ManureStateType.not_selected,
            manure_location_source_type: ManureLocationSourceType = ManureLocationSourceType.NotSelected

    ):
        """

        Args:
            name:
            field_area:
            current_year:
            crop_year:
            year_in_perennial_stand:
            crop_type:
            tillage_type:
            perennial_stand_id:
            perennial_stand_length:
            relative_biomass_information_data:
            crop_yield:
            harvest_method:
            nitrogen_fertilizer_rate:
            under_sown_crops_used:
            field_system_component_guid:
            province:
            clay_content:
            sand_content:
            organic_carbon_percentage:
            soil_top_layer_thickness:
            soil_functional_category:
            fertilizer_blend:
            evapotranspiration:
            precipitation:
            temperature:
            amount_of_irrigation:
            number_of_pesticide_passes:
            amount_of_manure_applied:
            manure_application_type:
            manure_animal_source_type:
            manure_state_type:
            manure_location_source_type:
        """
        super().__init__()

        self.name.value = name
        self.area.value = field_area
        self.current_year.value = current_year
        self.crop_year.value = crop_year
        self.crop_type.value = crop_type
        self.tillage_type.value = tillage_type
        self.year_in_perennial_stand.value = year_in_perennial_stand
        self.perennial_stand_id.value = str(perennial_stand_id)
        self.perennial_stand_length.value = perennial_stand_length

        self.initialize_biomass_coefficients(residue_data=relative_biomass_information_data)
        self.initialize_nitrogen_content(residue_data=relative_biomass_information_data)

        self.nitrogen_fixation.value = get_nitrogen_fixation(crop_type=crop_type)
        self.crop_yield.value = crop_yield
        self.harvest_method.value = harvest_method if harvest_method is not None else self.get_default_harvest_method()
        self.nitrogen_fertilizer_rate.value = nitrogen_fertilizer_rate

        self.amount_of_irrigation.value = amount_of_irrigation
        self.set_irrigation_type()

        self.moisture_content_of_crop.value = relative_biomass_information_data.MoistureContentOfProduct / 100
        self.set_moisture_content()
        self.set_percentage_returns()
        self.number_of_pesticide_passes.value = number_of_pesticide_passes
        self.is_pesticide_used.value = "Yes" if number_of_pesticide_passes > 0 else "No"

        self.amount_of_manure_applied.value = amount_of_manure_applied
        self.manure_applied.value = amount_of_manure_applied > 0
        self.manure_application_type.value = manure_application_type
        self.manure_animal_source_type.value = manure_animal_source_type
        self.manure_state_type.value = manure_state_type.value
        self.manure_location_source_type.value = manure_location_source_type
        self.under_sown_crops_used.value = str(under_sown_crops_used)
        self.field_system_component_guid.value = str(field_system_component_guid)

        self.fuel_energy.value = get_fuel_energy_estimate(
            province=province,
            soil_category=soil_functional_category,
            tillage_type=tillage_type,
            crop_type=crop_type)
        self.herbicide_energy.value = get_herbicide_energy_estimate(
            province=province,
            soil_category=soil_functional_category,
            tillage_type=tillage_type,
            crop_type=crop_type)
        self.fertilizer_blend.value = fertilizer_blend

        is_perennial = crop_type.is_perennial()
        self.climate_parameter.value = calculate_climate_parameter(
            emergence_day=Defaults.EmergenceDayForPerennials if is_perennial else Defaults.EmergenceDay,
            ripening_day=Defaults.RipeningDayForPerennials if is_perennial else Defaults.RipeningDay,
            crop_yield=crop_yield,
            clay=clay_content,
            sand=sand_content,
            layer_thickness_in_millimeters=soil_top_layer_thickness,
            percentage_soil_organic_carbon=organic_carbon_percentage,
            variance=Defaults.VarianceForPerennials if is_perennial else Defaults.Variance,
            alfa=Defaults.Alfa,
            decomposition_minimum_temperature=Defaults.DecompositionMinimumTemperature,
            decomposition_maximum_temperature=Defaults.DecompositionMaximumTemperature,
            moisture_response_function_at_wilting_point=Defaults.MoistureResponseFunctionAtWiltingPoint,
            moisture_response_function_at_saturation=Defaults.MoistureResponseFunctionAtSaturation,
            evapotranspirations=evapotranspiration,
            precipitations=precipitation,
            temperatures=temperature)
        self.tillage_factor.value = calculate_tillage_factor(
            province=province,
            soil_functional_category=soil_functional_category,
            tillage_type=tillage_type,
            crop_type=crop_type)
        self.management_factor.value = calculate_management_factor(
            climate_parameter=self.climate_parameter.value,
            tillage_factor=self.tillage_factor.value)

        self.sand.value = sand_content
        self.lignin.value = relative_biomass_information_data.LigninContent
