import unittest
from itertools import product

from holos_service.components.animals import common


class _AnimalGroups:
    young_type: list[common.AnimalType] = [
        common.AnimalType.beef_calf,
        common.AnimalType.dairy_calves,
        common.AnimalType.swine_piglets,
        common.AnimalType.weaned_lamb,
        common.AnimalType.lambs]

    beef_cattle_type: list[common.AnimalType] = [
        common.AnimalType.beef,
        common.AnimalType.beef_backgrounder,
        common.AnimalType.beef_bulls,
        common.AnimalType.beef_backgrounder_heifer,
        common.AnimalType.beef_finishing_steer,
        common.AnimalType.beef_finishing_heifer,
        common.AnimalType.beef_replacement_heifers,
        common.AnimalType.beef_finisher,
        common.AnimalType.beef_backgrounder_steer,
        common.AnimalType.beef_calf,
        common.AnimalType.stockers,
        common.AnimalType.stocker_heifers,
        common.AnimalType.stocker_steers,
        common.AnimalType.beef_cow_lactating,
        common.AnimalType.beef_cow,
        common.AnimalType.beef_cow_dry]

    dairy_cattle_type: list[common.AnimalType] = [
        common.AnimalType.dairy,
        common.AnimalType.dairy_lactating_cow,
        common.AnimalType.dairy_bulls,
        common.AnimalType.dairy_calves,
        common.AnimalType.dairy_dry_cow,
        common.AnimalType.dairy_heifers]

    swine_type: list[common.AnimalType] = [
        common.AnimalType.swine,
        common.AnimalType.swine_finisher,
        common.AnimalType.swine_starter,
        common.AnimalType.swine_lactating_sow,
        common.AnimalType.swine_dry_sow,
        common.AnimalType.swine_grower,
        common.AnimalType.swine_sows,
        common.AnimalType.swine_boar,
        common.AnimalType.swine_gilts,
        common.AnimalType.swine_piglets]

    sheep_type: list[common.AnimalType] = [
        common.AnimalType.sheep,
        common.AnimalType.lambs_and_ewes,
        common.AnimalType.ram,
        common.AnimalType.weaned_lamb,
        common.AnimalType.lambs,
        common.AnimalType.ewes,
        common.AnimalType.sheep_feedlot]

    poultry_type: list[common.AnimalType] = [
        common.AnimalType.poultry,
        common.AnimalType.layers_wet_poultry,
        common.AnimalType.layers_dry_poultry,
        common.AnimalType.layers,
        common.AnimalType.broilers,
        common.AnimalType.turkeys,
        common.AnimalType.ducks,
        common.AnimalType.geese,
        common.AnimalType.chicken_pullets,
        common.AnimalType.chicken_cockerels,
        common.AnimalType.chicken_roosters,
        common.AnimalType.chicken_hens,
        common.AnimalType.young_tom,
        common.AnimalType.tom,
        common.AnimalType.young_turkey_hen,
        common.AnimalType.turkey_hen,
        common.AnimalType.chicken_eggs,
        common.AnimalType.turkey_eggs,
        common.AnimalType.chicks,
        common.AnimalType.poults]

    other_animal_type: list[common.AnimalType] = [
        common.AnimalType.other_livestock,
        common.AnimalType.goats,
        common.AnimalType.alpacas,
        common.AnimalType.deer,
        common.AnimalType.elk,
        common.AnimalType.llamas,
        common.AnimalType.horses,
        common.AnimalType.mules,
        common.AnimalType.bison]

    chicken_type: list[common.AnimalType] = [
        common.AnimalType.chicken,
        common.AnimalType.chicken_hens,
        common.AnimalType.layers,
        common.AnimalType.broilers,
        common.AnimalType.chicken_roosters,
        common.AnimalType.chicken_pullets,
        common.AnimalType.chicken_cockerels,
        common.AnimalType.chicken_eggs,
        common.AnimalType.chicks]

    turkey_type: list[common.AnimalType] = [
        common.AnimalType.turkey_hen,
        common.AnimalType.young_turkey_hen,
        common.AnimalType.tom,
        common.AnimalType.turkey_eggs,
        common.AnimalType.young_tom,
        common.AnimalType.poults]

    layers_type: list[common.AnimalType] = [
        common.AnimalType.layers,
        common.AnimalType.layers_dry_poultry,
        common.AnimalType.layers_wet_poultry]

    lactating_type: list[common.AnimalType] = [
        common.AnimalType.beef_cow_lactating,
        common.AnimalType.beef_cow,
        common.AnimalType.dairy_lactating_cow,
        common.AnimalType.ewes]

    eggs_type: list[common.AnimalType] = [
        common.AnimalType.chicken_eggs,
        common.AnimalType.turkey_eggs]

    newly_hatched_type: list[common.AnimalType] = [
        common.AnimalType.poults,
        common.AnimalType.chicks]

    pregnant_type: list[common.AnimalType] = [
        common.AnimalType.beef_cow,
        common.AnimalType.beef_cow_lactating,
        common.AnimalType.dairy_lactating_cow,
        common.AnimalType.dairy_dry_cow,
        common.AnimalType.ewes]


class TestAnimalTypeExtensions(unittest.TestCase):
    def setUp(self):
        self.animal_groups = _AnimalGroups

    def test_is_young_type(self):
        for animal_type in self.animal_groups.young_type:
            self.assertTrue(animal_type.is_young_type)

    def test_is_beef_cattle_type(self):
        for animal_type in self.animal_groups.beef_cattle_type:
            self.assertTrue(animal_type.is_beef_cattle_type())

    def test_is_dairy_cattle_type(self):
        for animal_type in self.animal_groups.dairy_cattle_type:
            self.assertTrue(animal_type.is_dairy_cattle_type())

    def test_is_swine_type(self):
        for animal_type in self.animal_groups.swine_type:
            self.assertTrue(animal_type.is_swine_type())

    def test_is_sheep_type(self):
        for animal_type in self.animal_groups.sheep_type:
            self.assertTrue(animal_type.is_sheep_type())

    def test_is_poultry_type(self):
        for animal_type in self.animal_groups.poultry_type:
            self.assertTrue(animal_type.is_poultry_type())

    def test_is_other_animal_type(self):
        for animal_type in self.animal_groups.other_animal_type:
            self.assertTrue(animal_type.is_other_animal_type())

    def test_is_chicken_type(self):
        for animal_type in self.animal_groups.chicken_type:
            self.assertTrue(animal_type.is_chicken_type())

    def test_is_turkey_type(self):
        for animal_type in self.animal_groups.turkey_type:
            self.assertTrue(animal_type.is_turkey_type())

    def test_is_layers_type(self):
        for animal_type in self.animal_groups.layers_type:
            self.assertTrue(animal_type.is_layers_type())

    def test_is_lactating_type(self):
        for animal_type in self.animal_groups.lactating_type:
            self.assertTrue(animal_type.is_lactating_type())

    def test_is_eggs(self):
        for animal_type in self.animal_groups.eggs_type:
            self.assertTrue(animal_type.is_eggs())

    def test_is_newly_hatched_eggs(self):
        for animal_type in self.animal_groups.newly_hatched_type:
            self.assertTrue(animal_type.is_newly_hatched_eggs())

    def test_is_pregnant_type(self):
        for animal_type in self.animal_groups.pregnant_type:
            self.assertTrue(animal_type.is_pregnant_type())

    def test_get_category_returns_expected_result_when_is_other_animal_type(self):
        self.assertEqual(
            common.AnimalType.other_livestock,
            common.AnimalType.other_livestock.get_category())

    def test_get_category_returns_expected_result_when_is_poultry_type(self):
        self.assertEqual(
            common.AnimalType.poultry,
            common.AnimalType.poultry.get_category())

    def test_get_category_returns_expected_result_when_is_sheep_type(self):
        self.assertEqual(
            common.AnimalType.sheep,
            common.AnimalType.sheep.get_category())

    def test_get_category_returns_expected_result_when_is_swine_type(self):
        self.assertEqual(
            common.AnimalType.swine,
            common.AnimalType.swine.get_category())

    def test_get_category_returns_expected_result_when_is_dairy_cattle_type(self):
        self.assertEqual(
            common.AnimalType.dairy,
            common.AnimalType.dairy.get_category())

    def test_get_category_returns_expected_result_when_is_beef_cattle_type(self):
        for animal_type in [
            common.AnimalType.calf,
            common.AnimalType.cattle,
            common.AnimalType.chicken,
            common.AnimalType.cow_calf,
            common.AnimalType.not_selected,
            common.AnimalType.young_bulls
        ]:
            self.assertEqual(
                common.AnimalType.not_selected,
                animal_type.get_category())


class TestHousingTypeExtensions(unittest.TestCase):
    def test_is_free_stall(self):
        housing_type = common.HousingType.small_free_stall

        self.assertTrue(housing_type.is_free_stall())
        self.assertTrue(housing_type.is_electrical_consuming_housing_type())

        self.assertFalse(housing_type.is_tie_stall())
        self.assertFalse(housing_type.is_barn())
        self.assertFalse(housing_type.is_feed_lot())
        self.assertFalse(housing_type.is_indoor_housing())
        self.assertFalse(housing_type.is_pasture())

    def test_is_tie_stall(self):
        housing_type = common.HousingType.tie_stall

        self.assertTrue(housing_type.is_tie_stall())
        self.assertTrue(housing_type.is_electrical_consuming_housing_type())

        self.assertFalse(housing_type.is_free_stall())
        self.assertFalse(housing_type.is_barn())
        self.assertFalse(housing_type.is_feed_lot())
        self.assertFalse(housing_type.is_indoor_housing())
        self.assertFalse(housing_type.is_pasture())

    def test_is_barn(self):
        housing_type = common.HousingType.housed_in_barn

        self.assertTrue(housing_type.is_barn())
        self.assertTrue(housing_type.is_indoor_housing())
        self.assertTrue(housing_type.is_electrical_consuming_housing_type())

        self.assertFalse(housing_type.is_free_stall())
        self.assertFalse(housing_type.is_tie_stall())
        self.assertFalse(housing_type.is_feed_lot())
        self.assertFalse(housing_type.is_pasture())

    def test_is_feed_lot(self):
        housing_type = common.HousingType.confined

        self.assertTrue(housing_type.is_feed_lot())
        self.assertTrue(housing_type.is_electrical_consuming_housing_type())

        self.assertFalse(housing_type.is_free_stall())
        self.assertFalse(housing_type.is_tie_stall())
        self.assertFalse(housing_type.is_barn())
        self.assertFalse(housing_type.is_indoor_housing())
        self.assertFalse(housing_type.is_pasture())

    def test_is_pasture(self):
        housing_type = common.HousingType.pasture

        self.assertTrue(housing_type.is_pasture())

        self.assertFalse(housing_type.is_free_stall())
        self.assertFalse(housing_type.is_tie_stall())
        self.assertFalse(housing_type.is_barn())
        self.assertFalse(housing_type.is_feed_lot())
        self.assertFalse(housing_type.is_electrical_consuming_housing_type())
        self.assertFalse(housing_type.is_indoor_housing())


class TestBedding(unittest.TestCase):
    def setUp(self):
        self.animal_groups = _AnimalGroups

    def test_get_default_bedding_rate_for_pasture_rate_is_always_zero(self):
        for bedding_material_type, animal_type in product(common.BeddingMaterialType, common.AnimalType):
            bedding = common.Bedding(
                housing_type=common.HousingType.pasture,
                bedding_material_type=bedding_material_type,
                animal_type=animal_type)

            self.assertEqual(
                0,
                bedding.user_defined_bedding_rate.value)

    def test_get_default_bedding_rate_for_young_animals_is_always_zero(self):
        for housing_type, bedding_material_type, animal_type in product(
                common.HousingType,
                common.BeddingMaterialType,
                self.animal_groups.young_type):
            bedding = common.Bedding(
                housing_type=housing_type,
                bedding_material_type=bedding_material_type,
                animal_type=animal_type)

            self.assertEqual(
                0,
                bedding.user_defined_bedding_rate.value)

    def test_get_default_bedding_rate_for_beef_cattle_returns_expected_result(self):
        for animal_type in [v for v in self.animal_groups.beef_cattle_type if not v.is_young_type()]:
            for housing_type in (
                    common.HousingType.confined,
                    common.HousingType.confined_no_barn):
                self.assertEqual(
                    1.5,
                    common.Bedding(
                        housing_type=housing_type,
                        bedding_material_type=common.BeddingMaterialType.straw,
                        animal_type=animal_type).user_defined_bedding_rate.value)
                self.assertEqual(
                    3.6,
                    common.Bedding(
                        housing_type=housing_type,
                        bedding_material_type=common.BeddingMaterialType.wood_chip,
                        animal_type=animal_type).user_defined_bedding_rate.value)

            for housing_type in (
                    common.HousingType.housed_in_barn,
                    common.HousingType.housed_in_barn_slurry,
                    common.HousingType.housed_in_barn_solid):
                self.assertEqual(
                    3.5,
                    common.Bedding(
                        housing_type=housing_type,
                        bedding_material_type=common.BeddingMaterialType.straw,
                        animal_type=animal_type).user_defined_bedding_rate.value)
                self.assertEqual(
                    5,
                    common.Bedding(
                        housing_type=housing_type,
                        bedding_material_type=common.BeddingMaterialType.wood_chip,
                        animal_type=animal_type).user_defined_bedding_rate.value)

    def test_get_default_bedding_rate_for_dairy_cattle_returns_expected_result(self):
        for animal_type in [v for v in self.animal_groups.dairy_cattle_type if not v.is_young_type()]:

            for housing_type in (
                    common.HousingType.tie_stall,
                    common.HousingType.tie_stall_slurry,
                    common.HousingType.tie_stall_solid_litter,
                    common.HousingType.small_free_stall,
                    common.HousingType.large_free_stall,
                    common.HousingType.free_stall_barn_flushing,
                    common.HousingType.free_stall_barn_milk_parlour_slurry_flushing,
                    common.HousingType.free_stall_barn_slurry_scraping,
                    common.HousingType.free_stall_barn_solid_litter,
                    common.HousingType.dry_lot):
                self.assertEqual(
                    24.3,
                    common.Bedding(
                        housing_type=housing_type,
                        bedding_material_type=common.BeddingMaterialType.sand,
                        animal_type=animal_type).user_defined_bedding_rate.value)

                self.assertEqual(
                    0,
                    common.Bedding(
                        housing_type=housing_type,
                        bedding_material_type=common.BeddingMaterialType.separated_manure_solid,
                        animal_type=animal_type).user_defined_bedding_rate.value)

                self.assertEqual(
                    0.7,
                    common.Bedding(
                        housing_type=housing_type,
                        bedding_material_type=common.BeddingMaterialType.straw_long,
                        animal_type=animal_type).user_defined_bedding_rate.value)

                self.assertEqual(
                    0.7,
                    common.Bedding(
                        housing_type=housing_type,
                        bedding_material_type=common.BeddingMaterialType.straw_chopped,
                        animal_type=animal_type).user_defined_bedding_rate.value)

                self.assertEqual(
                    2.1,
                    common.Bedding(
                        housing_type=housing_type,
                        bedding_material_type=common.BeddingMaterialType.shavings,
                        animal_type=animal_type).user_defined_bedding_rate.value)

                self.assertEqual(
                    2.1,
                    common.Bedding(
                        housing_type=housing_type,
                        bedding_material_type=common.BeddingMaterialType.sawdust,
                        animal_type=animal_type).user_defined_bedding_rate.value)

    def test_get_default_bedding_rate_for_sheep_returns_expected_result(self):
        housing_types = [v for v in common.HousingType if not v.is_pasture()]
        for animal_type in [v for v in self.animal_groups.sheep_type if not v.is_young_type()]:
            for bedding_material_type, housing_type in product(
                    common.BeddingMaterialType,
                    housing_types):
                self.assertEqual(
                    0.57,
                    common.Bedding(
                        housing_type=housing_type,
                        bedding_material_type=bedding_material_type,
                        animal_type=animal_type).user_defined_bedding_rate.value)

    def test_get_default_bedding_rate_for_swine_returns_expected_result(self):
        housing_types = [v for v in common.HousingType if not v.is_pasture()]
        bedding_material_types = [v for v in common.BeddingMaterialType
                                  if not v == common.BeddingMaterialType.straw_long]
        animal_types = [v for v in self.animal_groups.swine_type if not v.is_young_type()]

        for housing_type, animal_type in product(
                housing_types,
                animal_types):

            self.assertEqual(
                0.7,
                common.Bedding(
                    housing_type=housing_type,
                    bedding_material_type=common.BeddingMaterialType.straw_long,
                    animal_type=animal_type).user_defined_bedding_rate.value)

            for bedding_material_type in bedding_material_types:
                self.assertEqual(
                    0.79,
                    common.Bedding(
                        housing_type=housing_type,
                        bedding_material_type=bedding_material_type,
                        animal_type=animal_type).user_defined_bedding_rate.value)

    def test_get_default_bedding_rate_for_poultry_returns_expected_result(self):
        housing_types = [v for v in common.HousingType if not v.is_pasture()]
        bedding_material_types = list(common.BeddingMaterialType)
        animal_types = [v for v in self.animal_groups.poultry_type if not v.is_young_type()]

        animal_types_to_exclude = []
        for housing_type in housing_types:
            for bedding_material_type in (
                    common.BeddingMaterialType.sawdust,
                    common.BeddingMaterialType.straw,
                    common.BeddingMaterialType.shavings):
                for animal_type, expected_value in (
                        (common.AnimalType.broilers, 0.0014),
                        (common.AnimalType.chicken_pullets, 0.0014),
                        (common.AnimalType.layers, 0.0028),
                        (common.AnimalType.chicken_hens, 0.0028),
                        (common.AnimalType.turkey_hen, 0.011),
                        (common.AnimalType.young_turkey_hen, 0.011),
                        (common.AnimalType.tom, 0.011),
                        (common.AnimalType.turkey_eggs, 0.011),
                        (common.AnimalType.young_tom, 0.011),
                        (common.AnimalType.poults, 0.011),
                ):
                    animal_types_to_exclude.append(animal_type)
                    self.assertEqual(
                        expected_value,
                        common.Bedding(
                            housing_type=housing_type,
                            bedding_material_type=bedding_material_type,
                            animal_type=animal_type).user_defined_bedding_rate.value)
        for animal_type, bedding_material_type, housing_type in product(
                [v for v in animal_types if v not in set(animal_types_to_exclude)],
                bedding_material_types,
                housing_types):
            self.assertEqual(
                0,
                common.Bedding(
                    housing_type=housing_type,
                    bedding_material_type=bedding_material_type,
                    animal_type=animal_type).user_defined_bedding_rate.value)

    def test_get_default_bedding_rate_for_other_animal_returns_expected_result(self):
        for housing_type, bedding_material_type in product(
                [v for v in common.HousingType if not v.is_pasture()],
                common.BeddingMaterialType):
            animal_types_to_exclude = []
            for animal_type, expected_value in (
                    (common.AnimalType.llamas, 0.57),
                    (common.AnimalType.alpacas, 0.57),
                    (common.AnimalType.deer, 1.5),
                    (common.AnimalType.elk, 1.5),
                    (common.AnimalType.goats, 0.57),
                    (common.AnimalType.horses, 1.5),
                    (common.AnimalType.mules, 1.5),
                    (common.AnimalType.bison, 1.5)):
                self.assertEqual(
                    expected_value,
                    common.Bedding(
                        housing_type=housing_type,
                        bedding_material_type=bedding_material_type,
                        animal_type=animal_type).user_defined_bedding_rate.value)

                animal_types_to_exclude.append(animal_type)

            for animal_type in self.animal_groups.other_animal_type:
                if all([
                    animal_type not in animal_types_to_exclude,
                    not animal_type.is_young_type()]):
                    self.assertEqual(
                        1,
                        common.Bedding(
                            housing_type=housing_type,
                            bedding_material_type=bedding_material_type,
                            animal_type=animal_type).user_defined_bedding_rate.value)

    def test_get_bedding_material_composition_for_beef_and_straw_returns_expected_results(self):
        self.assertEqual(
            dict(
                AnimalType=common.AnimalType.beef.value,
                BeddingMaterial=common.BeddingMaterialType.straw.value,
                TotalNitrogenKilogramsDryMatter=0.0057,
                TotalCarbonKilogramsDryMatter=0.447,
                TotalPhosphorusKilogramsDryMatter=0.000635,
                CarbonToNitrogenRatio=90.5,
                MoistureContent=9.57
            ),
            common.Bedding.get_bedding_material_composition(
                animal_type=common.AnimalType.beef,
                bedding_material_type=common.BeddingMaterialType.straw))

    def test_get_bedding_material_composition_for_beef_and_wood_chip_returns_expected_results(self):
        self.assertEqual(
            dict(
                AnimalType=common.AnimalType.beef.value,
                BeddingMaterial=common.BeddingMaterialType.wood_chip.value,
                TotalNitrogenKilogramsDryMatter=0.00185,
                TotalCarbonKilogramsDryMatter=0.506,
                TotalPhosphorusKilogramsDryMatter=0.000275,
                CarbonToNitrogenRatio=329.5,
                MoistureContent=12.82
            ),
            common.Bedding.get_bedding_material_composition(
                animal_type=common.AnimalType.beef,
                bedding_material_type=common.BeddingMaterialType.wood_chip))

    def test_get_bedding_material_composition_for_dairy_and_sand_returns_expected_results(self):

        self.assertEqual(
            dict(
                AnimalType=common.AnimalType.dairy.value,
                BeddingMaterial=common.BeddingMaterialType.sand.value,
                TotalNitrogenKilogramsDryMatter=None,
                TotalCarbonKilogramsDryMatter=None,
                TotalPhosphorusKilogramsDryMatter=None,
                CarbonToNitrogenRatio=None,
                MoistureContent=None
            ),
            common.Bedding.get_bedding_material_composition(
                animal_type=common.AnimalType.dairy,
                bedding_material_type=common.BeddingMaterialType.sand))

    def test_get_bedding_material_composition_for_dairy_and_separated_manure_solid_returns_expected_results(self):
        self.assertEqual(
            dict(
                AnimalType=common.AnimalType.dairy.value,
                BeddingMaterial=common.BeddingMaterialType.separated_manure_solid.value,
                TotalNitrogenKilogramsDryMatter=0.033,
                TotalCarbonKilogramsDryMatter=0.395,
                TotalPhosphorusKilogramsDryMatter=0,
                CarbonToNitrogenRatio=12,
                MoistureContent=0
            ),
            common.Bedding.get_bedding_material_composition(
                animal_type=common.AnimalType.dairy,
                bedding_material_type=common.BeddingMaterialType.separated_manure_solid))

    def test_get_bedding_material_composition_for_dairy_and_straw_long_returns_expected_results(self):
        self.assertEqual(
            dict(
                AnimalType=common.AnimalType.dairy.value,
                BeddingMaterial=common.BeddingMaterialType.straw_long.value,
                TotalNitrogenKilogramsDryMatter=0.0057,
                TotalCarbonKilogramsDryMatter=0.447,
                TotalPhosphorusKilogramsDryMatter=0.000635,
                CarbonToNitrogenRatio=90.5,
                MoistureContent=9.57
            ),
            common.Bedding.get_bedding_material_composition(
                animal_type=common.AnimalType.dairy,
                bedding_material_type=common.BeddingMaterialType.straw_long))

    def test_get_bedding_material_composition_for_dairy_and_straw_chopped_returns_expected_results(self):
        self.assertEqual(
            dict(
                AnimalType=common.AnimalType.dairy.value,
                BeddingMaterial=common.BeddingMaterialType.straw_chopped.value,
                TotalNitrogenKilogramsDryMatter=0.0057,
                TotalCarbonKilogramsDryMatter=0.447,
                TotalPhosphorusKilogramsDryMatter=0.000635,
                CarbonToNitrogenRatio=90.5,
                MoistureContent=9.57
            ),
            common.Bedding.get_bedding_material_composition(
                animal_type=common.AnimalType.dairy,
                bedding_material_type=common.BeddingMaterialType.straw_chopped))

    def test_get_bedding_material_composition_for_dairy_and_shavings_returns_expected_results(self):
        self.assertEqual(
            dict(
                AnimalType=common.AnimalType.dairy.value,
                BeddingMaterial=common.BeddingMaterialType.shavings.value,
                TotalNitrogenKilogramsDryMatter=0.00185,
                TotalCarbonKilogramsDryMatter=0.506,
                TotalPhosphorusKilogramsDryMatter=0.000275,
                CarbonToNitrogenRatio=329.5,
                MoistureContent=10.09
            ),
            common.Bedding.get_bedding_material_composition(
                animal_type=common.AnimalType.dairy,
                bedding_material_type=common.BeddingMaterialType.shavings))

    def test_get_bedding_material_composition_for_dairy_and_sawdust_returns_expected_results(self):
        self.assertEqual(
            dict(
                AnimalType=common.AnimalType.dairy.value,
                BeddingMaterial=common.BeddingMaterialType.sawdust.value,
                TotalNitrogenKilogramsDryMatter=0.00185,
                TotalCarbonKilogramsDryMatter=0.506,
                TotalPhosphorusKilogramsDryMatter=0.000275,
                CarbonToNitrogenRatio=329.5,
                MoistureContent=10.99
            ),
            common.Bedding.get_bedding_material_composition(
                animal_type=common.AnimalType.dairy,
                bedding_material_type=common.BeddingMaterialType.sawdust))

    def test_get_bedding_material_composition_for_swine_and_straw_long_returns_expected_results(self):
        self.assertEqual(
            dict(
                AnimalType=common.AnimalType.swine.value,
                BeddingMaterial=common.BeddingMaterialType.straw_long.value,
                TotalNitrogenKilogramsDryMatter=0.0057,
                TotalCarbonKilogramsDryMatter=0.447,
                TotalPhosphorusKilogramsDryMatter=0.000635,
                CarbonToNitrogenRatio=90.5,
                MoistureContent=9.57
            ),
            common.Bedding.get_bedding_material_composition(
                animal_type=common.AnimalType.swine,
                bedding_material_type=common.BeddingMaterialType.straw_long))

    def test_get_bedding_material_composition_for_swine_and_straw_chopped_returns_expected_results(self):
        self.assertEqual(
            dict(
                AnimalType=common.AnimalType.swine.value,
                BeddingMaterial=common.BeddingMaterialType.straw_chopped.value,
                TotalNitrogenKilogramsDryMatter=0.0057,
                TotalCarbonKilogramsDryMatter=0.447,
                TotalPhosphorusKilogramsDryMatter=0.000635,
                CarbonToNitrogenRatio=90.5,
                MoistureContent=9.57
            ),
            common.Bedding.get_bedding_material_composition(
                animal_type=common.AnimalType.swine,
                bedding_material_type=common.BeddingMaterialType.straw_chopped))

    def test_get_bedding_material_composition_for_sheep_and_straw_returns_expected_results(self):
        self.assertEqual(
            dict(
                AnimalType=common.AnimalType.sheep.value,
                BeddingMaterial=common.BeddingMaterialType.straw.value,
                TotalNitrogenKilogramsDryMatter=0.0057,
                TotalCarbonKilogramsDryMatter=0.447,
                TotalPhosphorusKilogramsDryMatter=0.000635,
                CarbonToNitrogenRatio=90.5,
                MoistureContent=9.57
            ),
            common.Bedding.get_bedding_material_composition(
                animal_type=common.AnimalType.sheep,
                bedding_material_type=common.BeddingMaterialType.straw))

    def test_get_bedding_material_composition_for_sheep_and_shavings_returns_expected_results(self):
        self.assertEqual(
            dict(
                AnimalType=common.AnimalType.sheep.value,
                BeddingMaterial=common.BeddingMaterialType.shavings.value,
                TotalNitrogenKilogramsDryMatter=0.00185,
                TotalCarbonKilogramsDryMatter=0.506,
                TotalPhosphorusKilogramsDryMatter=0.000275,
                CarbonToNitrogenRatio=329.5,
                MoistureContent=10.09
            ),
            common.Bedding.get_bedding_material_composition(
                animal_type=common.AnimalType.sheep,
                bedding_material_type=common.BeddingMaterialType.shavings))

    def test_get_bedding_material_composition_for_poultry_and_straw_returns_expected_results(self):
        self.assertEqual(
            dict(
                AnimalType=common.AnimalType.poultry.value,
                BeddingMaterial=common.BeddingMaterialType.straw.value,
                TotalNitrogenKilogramsDryMatter=0.0057,
                TotalCarbonKilogramsDryMatter=0.447,
                TotalPhosphorusKilogramsDryMatter=0.000635,
                CarbonToNitrogenRatio=90.5,
                MoistureContent=9.57
            ),
            common.Bedding.get_bedding_material_composition(
                animal_type=common.AnimalType.poultry,
                bedding_material_type=common.BeddingMaterialType.straw))

    def test_get_bedding_material_composition_for_poultry_and_shavings_returns_expected_results(self):
        self.assertEqual(
            dict(
                AnimalType=common.AnimalType.poultry.value,
                BeddingMaterial=common.BeddingMaterialType.shavings.value,
                TotalNitrogenKilogramsDryMatter=0.00185,
                TotalCarbonKilogramsDryMatter=0.506,
                TotalPhosphorusKilogramsDryMatter=0.000275,
                CarbonToNitrogenRatio=329.5,
                MoistureContent=10.09
            ),
            common.Bedding.get_bedding_material_composition(
                animal_type=common.AnimalType.poultry,
                bedding_material_type=common.BeddingMaterialType.shavings))

    def test_get_bedding_material_composition_for_poultry_and_sawdust_returns_expected_results(self):
        self.assertEqual(
            dict(
                AnimalType=common.AnimalType.poultry.value,
                BeddingMaterial=common.BeddingMaterialType.sawdust.value,
                TotalNitrogenKilogramsDryMatter=0.00185,
                TotalCarbonKilogramsDryMatter=0.506,
                TotalPhosphorusKilogramsDryMatter=0.000275,
                CarbonToNitrogenRatio=329.5,
                MoistureContent=10.99
            ),
            common.Bedding.get_bedding_material_composition(
                animal_type=common.AnimalType.poultry,
                bedding_material_type=common.BeddingMaterialType.sawdust))

    def test_get_bedding_material_composition_for_llamas_and_straw_returns_expected_results(self):
        self.assertEqual(
            dict(
                AnimalType=common.AnimalType.llamas.value,
                BeddingMaterial=common.BeddingMaterialType.straw.value,
                MoistureContent=9.57,
                TotalNitrogenKilogramsDryMatter=0.0057,
                TotalCarbonKilogramsDryMatter=0.447,
                TotalPhosphorusKilogramsDryMatter=0.000635,
                CarbonToNitrogenRatio=90.5
            ),
            common.Bedding.get_bedding_material_composition(
                animal_type=common.AnimalType.llamas,
                bedding_material_type=common.BeddingMaterialType.straw))

    def test_get_bedding_material_composition_for_alpacas_and_straw_returns_expected_results(self):
        self.assertEqual(
            dict(
                AnimalType=common.AnimalType.alpacas.value,
                BeddingMaterial=common.BeddingMaterialType.straw.value,
                MoistureContent=9.57,
                TotalNitrogenKilogramsDryMatter=0.0057,
                TotalCarbonKilogramsDryMatter=0.447,
                TotalPhosphorusKilogramsDryMatter=0.000635,
                CarbonToNitrogenRatio=90.5
            ),
            common.Bedding.get_bedding_material_composition(
                animal_type=common.AnimalType.alpacas,
                bedding_material_type=common.BeddingMaterialType.straw))

    def test_get_bedding_material_composition_for_deer_and_straw_returns_expected_results(self):
        self.assertEqual(
            dict(
                AnimalType=common.AnimalType.deer.value,
                BeddingMaterial=common.BeddingMaterialType.straw.value,
                MoistureContent=9.57,
                TotalNitrogenKilogramsDryMatter=0.0057,
                TotalCarbonKilogramsDryMatter=0.447,
                TotalPhosphorusKilogramsDryMatter=0.000635,
                CarbonToNitrogenRatio=90.5
            ),
            common.Bedding.get_bedding_material_composition(
                animal_type=common.AnimalType.deer,
                bedding_material_type=common.BeddingMaterialType.straw))

    def test_get_bedding_material_composition_for_elk_and_straw_returns_expected_results(self):
        self.assertEqual(
            dict(
                AnimalType=common.AnimalType.elk.value,
                BeddingMaterial=common.BeddingMaterialType.straw.value,
                MoistureContent=9.57,
                TotalNitrogenKilogramsDryMatter=0.0057,
                TotalCarbonKilogramsDryMatter=0.447,
                TotalPhosphorusKilogramsDryMatter=0.000635,
                CarbonToNitrogenRatio=90.5
            ),
            common.Bedding.get_bedding_material_composition(
                animal_type=common.AnimalType.elk,
                bedding_material_type=common.BeddingMaterialType.straw))

    def test_get_bedding_material_composition_for_goats_and_straw_returns_expected_results(self):
        self.assertEqual(
            dict(
                AnimalType=common.AnimalType.goats.value,
                BeddingMaterial=common.BeddingMaterialType.straw.value,
                MoistureContent=9.57,
                TotalNitrogenKilogramsDryMatter=0.0057,
                TotalCarbonKilogramsDryMatter=0.447,
                TotalPhosphorusKilogramsDryMatter=0.000635,
                CarbonToNitrogenRatio=90.5
            ),
            common.Bedding.get_bedding_material_composition(
                animal_type=common.AnimalType.goats,
                bedding_material_type=common.BeddingMaterialType.straw))

    def test_get_bedding_material_composition_for_horses_and_straw_returns_expected_results(self):
        self.assertEqual(
            dict(
                AnimalType=common.AnimalType.horses.value,
                BeddingMaterial=common.BeddingMaterialType.straw.value,
                MoistureContent=9.57,
                TotalNitrogenKilogramsDryMatter=0.0057,
                TotalCarbonKilogramsDryMatter=0.447,
                TotalPhosphorusKilogramsDryMatter=0.000635,
                CarbonToNitrogenRatio=90.5
            ),
            common.Bedding.get_bedding_material_composition(
                animal_type=common.AnimalType.horses,
                bedding_material_type=common.BeddingMaterialType.straw))

    def test_get_bedding_material_composition_for_mules_and_straw_returns_expected_results(self):
        self.assertEqual(
            dict(
                AnimalType=common.AnimalType.mules.value,
                BeddingMaterial=common.BeddingMaterialType.straw.value,
                MoistureContent=9.57,
                TotalNitrogenKilogramsDryMatter=0.0057,
                TotalCarbonKilogramsDryMatter=0.447,
                TotalPhosphorusKilogramsDryMatter=0.000635,
                CarbonToNitrogenRatio=90.5
            ),
            common.Bedding.get_bedding_material_composition(
                animal_type=common.AnimalType.mules,
                bedding_material_type=common.BeddingMaterialType.straw))

    def test_get_bedding_material_composition_for_bison_and_straw_returns_expected_results(self):
        self.assertEqual(
            dict(
                AnimalType=common.AnimalType.bison.value,
                BeddingMaterial=common.BeddingMaterialType.straw.value,
                MoistureContent=9.57,
                TotalNitrogenKilogramsDryMatter=0.0057,
                TotalCarbonKilogramsDryMatter=0.447,
                TotalPhosphorusKilogramsDryMatter=0.000635,
                CarbonToNitrogenRatio=90.5
            ),
            common.Bedding.get_bedding_material_composition(
                animal_type=common.AnimalType.bison,
                bedding_material_type=common.BeddingMaterialType.straw))


class TestGetMethaneProducingCapacityOfManure(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.animal_types_all = list(common.AnimalType)

    def setUp(self):
        self.animal_types = _AnimalGroups

    def run_test(
            self,
            animal_type: common.AnimalType,
            expected_value: float
    ):
        self.assertEqual(
            expected_value,
            common.get_methane_producing_capacity_of_manure(animal_type=animal_type))

        self.animal_types_all.pop(self.animal_types_all.index(animal_type))
        pass

    def test_get_methane_producing_capacity_of_manure_returns_expected_values_when_is_beef_cattle_type(self):
        for animal_type in self.animal_types.beef_cattle_type:
            self.run_test(animal_type=animal_type, expected_value=0.19)

    def test_get_methane_producing_capacity_of_manure_returns_expected_values_when_is_dairy_cattle_type(self):
        for animal_type in self.animal_types.dairy_cattle_type:
            self.run_test(animal_type=animal_type, expected_value=0.24)

    def test_get_methane_producing_capacity_of_manure_returns_expected_values_when_is_swine_type(self):
        for animal_type in self.animal_types.swine_type:
            self.run_test(animal_type=animal_type, expected_value=0.48)

    def test_get_methane_producing_capacity_of_manure_returns_expected_values_when_is_sheep_type(self):
        for animal_type in self.animal_types.sheep_type:
            self.run_test(animal_type=animal_type, expected_value=0.19)

    def test_get_methane_producing_capacity_of_manure_returns_expected_values_for_chicken_roosters_and_broilers(self):
        for animal_type in [
            common.AnimalType.chicken_roosters,
            common.AnimalType.broilers
        ]:
            self.run_test(animal_type=animal_type, expected_value=0.36)

    def test_get_methane_producing_capacity_of_manure_returns_expected_values_for_chicken_hens_pullets_cockerels_layers(
            self):
        for animal_type in [
            common.AnimalType.chicken_hens,
            common.AnimalType.chicken_pullets,
            common.AnimalType.chicken_cockerels,
            common.AnimalType.layers
        ]:
            self.run_test(animal_type=animal_type, expected_value=0.39)

    def test_get_methane_producing_capacity_of_manure_returns_expected_values_for_goats(self):
        self.run_test(animal_type=common.AnimalType.goats, expected_value=0.18)

    def test_get_methane_producing_capacity_of_manure_returns_expected_values_for_horses(self):
        self.run_test(animal_type=common.AnimalType.horses, expected_value=0.30)

    def test_get_methane_producing_capacity_of_manure_returns_expected_values_for_mules(self):
        self.run_test(animal_type=common.AnimalType.mules, expected_value=0.33)

    def test_get_methane_producing_capacity_of_manure_returns_expected_values_for_llamas_and_alpacas(self):
        for animal_type in [
            common.AnimalType.llamas,
            common.AnimalType.alpacas
        ]:
            self.run_test(animal_type=animal_type, expected_value=0.19)

    def test_get_methane_producing_capacity_of_manure_returns_expected_values_for_bison(self):
        self.run_test(animal_type=common.AnimalType.bison, expected_value=0.1)

    def test_z_get_methane_producing_capacity_of_manure_returns_expected_default_value(self):
        for animal_type in self.animal_types_all:
            self.run_test(animal_type=animal_type, expected_value=0)


class TestGetDefaultMethaneProducingCapacityOfManure(unittest.TestCase):
    def test_get_default_methane_producing_capacity_of_manure_is_constant_for_pasture(self):
        for animal_type in common.AnimalType:
            self.assertEqual(
                0.19,
                common.get_default_methane_producing_capacity_of_manure(is_pasture=True, animal_type=animal_type))


class TestFractionOfOrganicNitrogenMineralizedData(unittest.TestCase):
    def testDefaultValues(self):
        self.assertEqual(
            {None},
            set(common.FractionOfOrganicNitrogenMineralizedData().__dict__.values())
        )


class TestGetFractionOfOrganicNitrogenMineralizedData(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.animal_types = _AnimalGroups
        cls.animal_types_not_beef_or_dairy = [v for v in common.AnimalType if
                                              not any([v.is_beef_cattle_type(), v.is_dairy_cattle_type()])]
        cls.manure_state_type_for_default_values = [v for v in common.ManureStateType if v not in (
            common.ManureStateType.liquid_with_natural_crust,
            common.ManureStateType.liquid_with_solid_cover,
            common.ManureStateType.deep_pit,
            common.ManureStateType.liquid_no_crust)]

    def test_values_when_is_beef_cattle_type_and_manure_handling_is_compost(self):
        for animal_type in self.animal_types.beef_cattle_type:
            for manure_state in (common.ManureStateType.compost_intensive,
                                 common.ManureStateType.compost_passive):
                self.assertEqual(
                    common.FractionOfOrganicNitrogenMineralizedData(
                        fraction_immobilized=0,
                        fraction_mineralized=0.46,
                        fraction_nitrified=0.25,
                        fraction_denitrified=0,
                        n2o_n=0.033,
                        no_n=0.0033,
                        n2_n=0.099,
                        n_leached=0.0575),
                    common.get_fraction_of_organic_nitrogen_mineralized_data(
                        state_type=manure_state,
                        animal_type=animal_type))

    def test_function_values_when_is_beef_cattle_type_and_manure_handling_is_deep_bedding_or_solid_storage(self):
        for animal_type in self.animal_types.beef_cattle_type:
            for manure_state in (common.ManureStateType.deep_bedding,
                                 common.ManureStateType.solid_storage):
                self.assertEqual(
                    common.FractionOfOrganicNitrogenMineralizedData(
                        fraction_immobilized=0,
                        fraction_mineralized=0.28,
                        fraction_nitrified=0.125,
                        fraction_denitrified=0,
                        n2o_n=0.033,
                        no_n=0.0033,
                        n2_n=0.099,
                        n_leached=0.0575),
                    common.get_fraction_of_organic_nitrogen_mineralized_data(
                        state_type=manure_state,
                        animal_type=animal_type))

    def test_values_when_is_dairy_cattle_type_and_manure_handling_is_compost(self):
        for animal_type in self.animal_types.dairy_cattle_type:
            for manure_state in (common.ManureStateType.compost_intensive,
                                 common.ManureStateType.compost_passive):
                self.assertEqual(
                    common.FractionOfOrganicNitrogenMineralizedData(
                        fraction_immobilized=0,
                        fraction_mineralized=0.46,
                        fraction_nitrified=0.282,
                        fraction_denitrified=0.152,
                        n2o_n=0.037,
                        no_n=0.0037,
                        n2_n=0.111,
                        n_leached=0.13),
                    common.get_fraction_of_organic_nitrogen_mineralized_data(
                        state_type=manure_state,
                        animal_type=animal_type))

    def test_values_when_is_dairy_cattle_type_and_manure_handling_is_deep_bedding_or_solid_storage(self):
        for animal_type in self.animal_types.dairy_cattle_type:
            for manure_state in (common.ManureStateType.deep_bedding,
                                 common.ManureStateType.solid_storage):
                self.assertEqual(
                    common.FractionOfOrganicNitrogenMineralizedData(
                        fraction_immobilized=0,
                        fraction_mineralized=0.28,
                        fraction_nitrified=0.141,
                        fraction_denitrified=0.076,
                        n2o_n=0.0185,
                        no_n=0.0019,
                        n2_n=0.0555,
                        n_leached=0.065),
                    common.get_fraction_of_organic_nitrogen_mineralized_data(
                        state_type=manure_state,
                        animal_type=animal_type))

    def test_values_when_animal_type_is_not_beef_or_dairy_cattle_type_and_manure_handling_is_case_1(self):
        for animal_type in self.animal_types_not_beef_or_dairy:
            for manure_state in (common.ManureStateType.liquid_with_natural_crust,
                                 common.ManureStateType.liquid_with_solid_cover,
                                 common.ManureStateType.deep_pit):
                self.assertEqual(
                    common.FractionOfOrganicNitrogenMineralizedData(
                        fraction_immobilized=0,
                        fraction_mineralized=0.1,
                        fraction_nitrified=0.021,
                        fraction_denitrified=0.021,
                        n2o_n=0.005,
                        no_n=0.0005,
                        n2_n=0.015,
                        n_leached=0),
                    common.get_fraction_of_organic_nitrogen_mineralized_data(
                        state_type=manure_state,
                        animal_type=animal_type))

    def test_values_when_animal_type_is_not_beef_or_dairy_cattle_type_and_manure_handling_is_case_2(self):
        for animal_type in self.animal_types_not_beef_or_dairy:
            self.assertEqual(
                common.FractionOfOrganicNitrogenMineralizedData(
                    fraction_immobilized=0,
                    fraction_mineralized=0.1,
                    fraction_nitrified=0.0,
                    fraction_denitrified=0,
                    n2o_n=0,
                    no_n=0,
                    n2_n=0,
                    n_leached=0),
                common.get_fraction_of_organic_nitrogen_mineralized_data(
                    state_type=common.ManureStateType.liquid_no_crust,
                    animal_type=animal_type))

    def test_default_value(self):
        for animal_type, manure_state in product(self.animal_types_not_beef_or_dairy,
                                                 self.manure_state_type_for_default_values):
            self.assertEqual(
                common.FractionOfOrganicNitrogenMineralizedData(),
                common.get_fraction_of_organic_nitrogen_mineralized_data(
                    state_type=manure_state,
                    animal_type=animal_type))


if __name__ == '__main__':
    unittest.main()
