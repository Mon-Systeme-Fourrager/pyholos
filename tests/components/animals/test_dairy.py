import unittest
from datetime import date
from pathlib import Path

from holos_service.components.animals import common, dairy
from holos_service.django_stuff import CanadianProvince
from holos_service.soil import SoilTexture
from holos_service.utils import read_holos_resource_table


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.non_regression_data = read_holos_resource_table(
            path_file=Path(__file__).parents[2] / 'sources/holos/non_regression_dairy.csv')
        cls.non_regression_data.set_index("Group Name", inplace=True)

        cls.manure_emission_kwargs = dict(
            mean_annual_precipitation=541.5,
            mean_annual_temperature=3.6,
            mean_annual_evapotranspiration=625.7,
            growing_season_precipitation=383,
            growing_season_evapotranspiration=568,
            province=CanadianProvince.Alberta,
            soil_texture=SoilTexture.Fine)

    def run_test(
            self,
            group_name: str,
            res: dict
    ):
        for k, v in self.non_regression_data.loc[group_name].to_dict().items():
            if v != res[k]:
                self.assertAlmostEqual(
                    v,
                    res[k],
                    places=3)

    def test_dairy_heifers(self):
        manure_state_type = common.ManureStateType.daily_spread

        dairy_heifers = dairy.DairyHeifers(
            management_period_name='Management period 1',
            group_pairing_number=0,
            management_period_start_date=date(2025, 1, 1),
            management_period_days=30,
            number_of_animals=20,
            production_stage=common.ProductionStage.gestating,
            number_of_young_animals=0,
            milk_data=common.Milk(),
            diet=common.Diet(
                crude_protein_percentage=16.146,
                forage_percentage=77.8,
                total_digestible_nutrient_percentage=69.516,
                ash_percentage=6.323,
                starch_percentage=0,
                fat_percentage=0,
                neutral_detergent_fiber_percentage=35.289,
                metabolizable_energy=2.4459),
            housing_type=common.HousingType.free_stall_barn_solid_litter,
            manure_handling_system=manure_state_type,
            manure_emission_factors=common.get_manure_emission_factors(
                animal_type=common.AnimalType.dairy_heifers,
                year=2025,
                manure_state_type=manure_state_type,
                **self.manure_emission_kwargs),
            bedding_material_type=common.BeddingMaterialType.sand
        )

        self.run_test(
            group_name=dairy_heifers.group_name.value,
            res=dairy_heifers.to_dict()
        )


if __name__ == '__main__':
    unittest.main()
