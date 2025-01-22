from holos_service.common import HolosVar
from holos_service.defaults import Defaults
from holos_service.components.land_management.carbon.relative_biomass_information import RelativeBiomassInformationData
from holos_service.components.land_management.common import (
    TillageType, HarvestMethod, IrrigationType, TimePeriodCategory)
from holos_service.components.land_management.crop import get_nitrogen_fixation, CropType
from holos_service.core_constants import CoreConstants


class LandManagementBase:
    def __init__(self):
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

        self.sand = HolosVar(name='Sand', value=0)
        """deprecated"""

        self.lignin = HolosVar(name='Lignin', value=0)
        """deprecated"""

        self.w_fac = HolosVar(name='WFac', value=0)
        """deprecated"""

        self.t_fac = HolosVar(name='TFac', value=0)
        """deprecated"""

        self.total_nitrogen_inputs_for_ipcc_tier2 = HolosVar(name='Total Nitrogen Inputs For Ipcc Tier 2', value=0)
        """deprecated"""

        self.nitrogen_content = HolosVar(name='Nitrogen Content', value=0)
        """deprecated"""

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
                moisture_content_of_crop_percentage = self.moisture_content_of_crop.value
            else:
                moisture_content_of_crop_percentage = 12

        self.moisture_content_of_crop_percentage.value = moisture_content_of_crop_percentage

    def set_percentage_returns(self):
        """

        Returns:

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

