import unittest
from itertools import product

from holos_service.components.animals import common
from holos_service.components.animals.common import (Bedding, BeddingMaterialType, AnimalType,
                                                     get_methane_producing_capacity_of_manure,
                                                     get_default_methane_producing_capacity_of_manure)


class TestAnimalTypeExtensions(unittest.TestCase):
    def test_is_young_type(self):
        for animal_type in [
            common.AnimalType.beef_calf,
            common.AnimalType.dairy_calves,
            common.AnimalType.swine_piglets,
            common.AnimalType.weaned_lamb,
            common.AnimalType.lambs
        ]:
            animal_type_extensions = common.AnimalTypeExtensions(animal_type=animal_type)
            self.assertTrue(animal_type_extensions.is_young_type)

    def test_is_beef_cattle_type(self):
        for animal_type in [
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
            common.AnimalType.beef_cow_dry
        ]:
            animal_type_extensions = common.AnimalTypeExtensions(animal_type=animal_type)
            self.assertTrue(animal_type_extensions.is_beef_cattle_type)

    def test_is_dairy_cattle_type(self):
        for animal_type in [
            common.AnimalType.dairy,
            common.AnimalType.dairy_lactating_cow,
            common.AnimalType.dairy_bulls,
            common.AnimalType.dairy_calves,
            common.AnimalType.dairy_dry_cow,
            common.AnimalType.dairy_heifers
        ]:
            animal_type_extensions = common.AnimalTypeExtensions(animal_type=animal_type)
            self.assertTrue(animal_type_extensions.is_dairy_cattle_type)

    def test_is_swine_type(self):
        for animal_type in [
            common.AnimalType.swine,
            common.AnimalType.swine_finisher,
            common.AnimalType.swine_starter,
            common.AnimalType.swine_lactating_sow,
            common.AnimalType.swine_dry_sow,
            common.AnimalType.swine_grower,
            common.AnimalType.swine_sows,
            common.AnimalType.swine_boar,
            common.AnimalType.swine_gilts,
            common.AnimalType.swine_piglets
        ]:
            animal_type_extensions = common.AnimalTypeExtensions(animal_type=animal_type)
            self.assertTrue(animal_type_extensions.is_swine_type)

    def test_is_sheep_type(self):
        for animal_type in [
            common.AnimalType.sheep,
            common.AnimalType.lambs_and_ewes,
            common.AnimalType.ram,
            common.AnimalType.weaned_lamb,
            common.AnimalType.lambs,
            common.AnimalType.ewes,
            common.AnimalType.sheep_feedlot
        ]:
            animal_type_extensions = common.AnimalTypeExtensions(animal_type=animal_type)
            self.assertTrue(animal_type_extensions.is_sheep_type)

    def test_is_poultry_type(self):
        for animal_type in [
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
            common.AnimalType.poults
        ]:
            animal_type_extensions = common.AnimalTypeExtensions(animal_type=animal_type)
            self.assertTrue(animal_type_extensions.is_poultry_type)

    def test_is_other_animal_type(self):
        for animal_type in [
            common.AnimalType.other_livestock,
            common.AnimalType.goats,
            common.AnimalType.alpacas,
            common.AnimalType.deer,
            common.AnimalType.elk,
            common.AnimalType.llamas,
            common.AnimalType.horses,
            common.AnimalType.mules,
            common.AnimalType.bison
        ]:
            animal_type_extensions = common.AnimalTypeExtensions(animal_type=animal_type)
            self.assertTrue(animal_type_extensions.is_other_animal_type)

    def test_is_chicken_type(self):
        for animal_type in [
            common.AnimalType.chicken,
            common.AnimalType.chicken_hens,
            common.AnimalType.layers,
            common.AnimalType.broilers,
            common.AnimalType.chicken_roosters,
            common.AnimalType.chicken_pullets,
            common.AnimalType.chicken_cockerels,
            common.AnimalType.chicken_eggs,
            common.AnimalType.chicks
        ]:
            animal_type_extensions = common.AnimalTypeExtensions(animal_type=animal_type)
            self.assertTrue(animal_type_extensions.is_chicken_type)

    def test_is_turkey_type(self):
        for animal_type in [
            common.AnimalType.turkey_hen,
            common.AnimalType.young_turkey_hen,
            common.AnimalType.tom,
            common.AnimalType.turkey_eggs,
            common.AnimalType.young_tom,
            common.AnimalType.poults
        ]:
            animal_type_extensions = common.AnimalTypeExtensions(animal_type=animal_type)
            self.assertTrue(animal_type_extensions.is_turkey_type)

    def test_is_layers_type(self):
        for animal_type in [
            common.AnimalType.layers,
            common.AnimalType.layers_dry_poultry,
            common.AnimalType.layers_wet_poultry
        ]:
            animal_type_extensions = common.AnimalTypeExtensions(animal_type=animal_type)
            self.assertTrue(animal_type_extensions.is_layers_type)

    def test_is_lactating_type(self):
        for animal_type in [
            common.AnimalType.beef_cow_lactating,
            common.AnimalType.beef_cow,
            common.AnimalType.dairy_lactating_cow,
            common.AnimalType.ewes
        ]:
            animal_type_extensions = common.AnimalTypeExtensions(animal_type=animal_type)
            self.assertTrue(animal_type_extensions.is_lactating_type)

    def test_is_eggs(self):
        for animal_type in [
            common.AnimalType.chicken_eggs,
            common.AnimalType.turkey_eggs
        ]:
            animal_type_extensions = common.AnimalTypeExtensions(animal_type=animal_type)
            self.assertTrue(animal_type_extensions.is_eggs)

    def test_is_newly_hatched_eggs(self):
        for animal_type in [
            common.AnimalType.poults,
            common.AnimalType.chicks
        ]:
            animal_type_extensions = common.AnimalTypeExtensions(animal_type=animal_type)
            self.assertTrue(animal_type_extensions.is_newly_hatched_eggs)

    def test_is_pregnant_type(self):
        for animal_type in [
            common.AnimalType.beef_cow,
            common.AnimalType.beef_cow_lactating,
            common.AnimalType.dairy_lactating_cow,
            common.AnimalType.dairy_dry_cow,
            common.AnimalType.ewes
        ]:
            animal_type_extensions = common.AnimalTypeExtensions(animal_type=animal_type)
            self.assertTrue(animal_type_extensions.is_pregnant_type)

    def test_get_category_returns_expected_result_when_is_other_animal_type(self):
        animal_type_extensions = common.AnimalTypeExtensions(animal_type=common.AnimalType.other_livestock)
        self.assertEqual(
            common.AnimalType.other_livestock,
            animal_type_extensions.get_category())

    def test_get_category_returns_expected_result_when_is_poultry_type(self):
        animal_type_extensions = common.AnimalTypeExtensions(animal_type=common.AnimalType.poultry)
        self.assertEqual(
            common.AnimalType.poultry,
            animal_type_extensions.get_category())

    def test_get_category_returns_expected_result_when_is_sheep_type(self):
        animal_type_extensions = common.AnimalTypeExtensions(animal_type=common.AnimalType.sheep)
        self.assertEqual(
            common.AnimalType.sheep,
            animal_type_extensions.get_category())

    def test_get_category_returns_expected_result_when_is_swine_type(self):
        animal_type_extensions = common.AnimalTypeExtensions(animal_type=common.AnimalType.swine)
        self.assertEqual(
            common.AnimalType.swine,
            animal_type_extensions.get_category())

    def test_get_category_returns_expected_result_when_is_dairy_cattle_type(self):
        animal_type_extensions = common.AnimalTypeExtensions(animal_type=common.AnimalType.dairy)
        self.assertEqual(
            common.AnimalType.dairy,
            animal_type_extensions.get_category())

    def test_get_category_returns_expected_result_when_is_beef_cattle_type(self):
        for animal_type in [
            common.AnimalType.calf,
            common.AnimalType.cattle,
            common.AnimalType.chicken,
            common.AnimalType.cow_calf,
            common.AnimalType.not_selected,
            common.AnimalType.young_bulls
        ]:
            animal_type_extensions = common.AnimalTypeExtensions(animal_type=animal_type)
            self.assertEqual(
                common.AnimalType.not_selected,
                animal_type_extensions.get_category())


class TestHousingTypeExtensions(unittest.TestCase):
    def test_is_free_stall(self):
        housing_type = common.HousingType.small_free_stall
        ext = common.HousingTypeExtensions(housing_type)

        self.assertTrue(ext.is_free_stall)
        self.assertTrue(ext.is_electrical_consuming_housing_type)

        self.assertFalse(ext.is_tie_stall)
        self.assertFalse(ext.is_barn)
        self.assertFalse(ext.is_feed_lot)
        self.assertFalse(ext.is_indoor_housing)
        self.assertFalse(ext.is_pasture)

    def test_is_tie_stall(self):
        housing_type = common.HousingType.tie_stall
        ext = common.HousingTypeExtensions(housing_type)

        self.assertTrue(ext.is_tie_stall)
        self.assertTrue(ext.is_electrical_consuming_housing_type)

        self.assertFalse(ext.is_free_stall)
        self.assertFalse(ext.is_barn)
        self.assertFalse(ext.is_feed_lot)
        self.assertFalse(ext.is_indoor_housing)
        self.assertFalse(ext.is_pasture)

    def test_is_barn(self):
        housing_type = common.HousingType.housed_in_barn
        ext = common.HousingTypeExtensions(housing_type)

        self.assertTrue(ext.is_barn)
        self.assertTrue(ext.is_indoor_housing)
        self.assertTrue(ext.is_electrical_consuming_housing_type)

        self.assertFalse(ext.is_free_stall)
        self.assertFalse(ext.is_tie_stall)
        self.assertFalse(ext.is_feed_lot)
        self.assertFalse(ext.is_pasture)

    def test_is_feed_lot(self):
        housing_type = common.HousingType.confined
        ext = common.HousingTypeExtensions(housing_type)

        self.assertTrue(ext.is_feed_lot)
        self.assertTrue(ext.is_electrical_consuming_housing_type)

        self.assertFalse(ext.is_free_stall)
        self.assertFalse(ext.is_tie_stall)
        self.assertFalse(ext.is_barn)
        self.assertFalse(ext.is_indoor_housing)
        self.assertFalse(ext.is_pasture)

    def test_is_pasture(self):
        housing_type = common.HousingType.pasture
        ext = common.HousingTypeExtensions(housing_type)

        self.assertTrue(ext.is_pasture)

        self.assertFalse(ext.is_free_stall)
        self.assertFalse(ext.is_tie_stall)
        self.assertFalse(ext.is_barn)
        self.assertFalse(ext.is_feed_lot)
        self.assertFalse(ext.is_electrical_consuming_housing_type)
        self.assertFalse(ext.is_indoor_housing)


class TestBedding(unittest.TestCase):

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
                [common.AnimalType.beef_calf,
                 common.AnimalType.dairy_calves,
                 common.AnimalType.swine_piglets,
                 common.AnimalType.weaned_lamb,
                 common.AnimalType.lambs]):
            bedding = common.Bedding(
                housing_type=housing_type,
                bedding_material_type=bedding_material_type,
                animal_type=animal_type)

            self.assertEqual(
                0,
                bedding.user_defined_bedding_rate.value)

    def test_get_default_bedding_rate_for_beef_cattle_returns_expected_result(self):
        for animal_type in (
                common.AnimalType.beef,
                common.AnimalType.beef_backgrounder,
                common.AnimalType.beef_bulls,
                common.AnimalType.beef_backgrounder_heifer,
                common.AnimalType.beef_finishing_steer,
                common.AnimalType.beef_finishing_heifer,
                common.AnimalType.beef_replacement_heifers,
                common.AnimalType.beef_finisher,
                common.AnimalType.beef_backgrounder_steer,
                # common.AnimalType.beef_calf,
                common.AnimalType.stockers,
                common.AnimalType.stocker_heifers,
                common.AnimalType.stocker_steers,
                common.AnimalType.beef_cow_lactating,
                common.AnimalType.beef_cow,
                common.AnimalType.beef_cow_dry):

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
        for animal_type in (
                common.AnimalType.dairy,
                common.AnimalType.dairy_lactating_cow,
                common.AnimalType.dairy_bulls,
                # common.AnimalType.dairy_calves,
                common.AnimalType.dairy_dry_cow,
                common.AnimalType.dairy_heifers):

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
        housing_types = [v for v in common.HousingType if not common.HousingTypeExtensions(v).is_pasture]
        for animal_type in (
                common.AnimalType.sheep,
                common.AnimalType.lambs_and_ewes,
                common.AnimalType.ram,
                # common.AnimalType.weaned_lamb,
                # common.AnimalType.lambs,
                common.AnimalType.ewes,
                common.AnimalType.sheep_feedlot):

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
        housing_types = [v for v in common.HousingType if not common.HousingTypeExtensions(v).is_pasture]
        bedding_material_types = [v for v in common.BeddingMaterialType
                                  if not v == common.BeddingMaterialType.straw_long]
        animal_types = [v for v in (
            common.AnimalType.swine,
            common.AnimalType.swine_finisher,
            common.AnimalType.swine_starter,
            common.AnimalType.swine_lactating_sow,
            common.AnimalType.swine_dry_sow,
            common.AnimalType.swine_grower,
            common.AnimalType.swine_sows,
            common.AnimalType.swine_boar,
            common.AnimalType.swine_gilts,
            common.AnimalType.swine_piglets)
                        if not common.AnimalTypeExtensions(v).is_young_type]

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
        housing_types = [v for v in common.HousingType if not common.HousingTypeExtensions(v).is_pasture]
        bedding_material_types = list(common.BeddingMaterialType)
        animal_types = [v for v in (
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
            common.AnimalType.poults)
                        if not common.AnimalTypeExtensions(v).is_young_type]

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
        animal_types = [
            common.AnimalType.other_livestock,
            common.AnimalType.goats,
            common.AnimalType.alpacas,
            common.AnimalType.deer,
            common.AnimalType.elk,
            common.AnimalType.llamas,
            common.AnimalType.horses,
            common.AnimalType.mules,
            common.AnimalType.bison]

        for housing_type, bedding_material_type in product(
                [v for v in common.HousingType if not common.HousingTypeExtensions(v).is_pasture],
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
            for animal_type in animal_types:
                if all([
                    animal_type not in animal_types_to_exclude,
                    not common.AnimalTypeExtensions(animal_type).is_young_type]):
                    self.assertEqual(
                        1,
                        common.Bedding(
                            housing_type=housing_type,
                            bedding_material_type=bedding_material_type,
                            animal_type=animal_type).user_defined_bedding_rate.value)

    def test_get_bedding_material_composition_for_beef_and_straw_returns_expected_results(self):
        self.assertEqual(
            dict(
                AnimalType=AnimalType.beef.value,
                BeddingMaterial=BeddingMaterialType.straw.value,
                TotalNitrogenKilogramsDryMatter=0.0057,
                TotalCarbonKilogramsDryMatter=0.447,
                TotalPhosphorusKilogramsDryMatter=0.000635,
                CarbonToNitrogenRatio=90.5,
                MoistureContent=9.57
            ),
            Bedding.get_bedding_material_composition(
                animal_type=AnimalType.beef,
                bedding_material_type=BeddingMaterialType.straw.value))

    def test_get_bedding_material_composition_for_beef_and_wood_chip_returns_expected_results(self):
        self.assertEqual(
            dict(
                AnimalType=AnimalType.beef.value,
                BeddingMaterial=BeddingMaterialType.wood_chip.value,
                TotalNitrogenKilogramsDryMatter=0.00185,
                TotalCarbonKilogramsDryMatter=0.506,
                TotalPhosphorusKilogramsDryMatter=0.000275,
                CarbonToNitrogenRatio=329.5,
                MoistureContent=12.82
            ),
            Bedding.get_bedding_material_composition(
                animal_type=AnimalType.beef,
                bedding_material_type=BeddingMaterialType.wood_chip.value))

    def test_get_bedding_material_composition_for_dairy_and_sand_returns_expected_results(self):

        self.assertEqual(
            dict(
                AnimalType=AnimalType.dairy.value,
                BeddingMaterial=BeddingMaterialType.sand.value,
                TotalNitrogenKilogramsDryMatter=None,
                TotalCarbonKilogramsDryMatter=None,
                TotalPhosphorusKilogramsDryMatter=None,
                CarbonToNitrogenRatio=None,
                MoistureContent=None
            ),
            Bedding.get_bedding_material_composition(
                animal_type=AnimalType.dairy,
                bedding_material_type=BeddingMaterialType.sand.value))

    def test_get_bedding_material_composition_for_dairy_and_separated_manure_solid_returns_expected_results(self):
        self.assertEqual(
            dict(
                AnimalType=AnimalType.dairy.value,
                BeddingMaterial=BeddingMaterialType.separated_manure_solid.value,
                TotalNitrogenKilogramsDryMatter=0.033,
                TotalCarbonKilogramsDryMatter=0.395,
                TotalPhosphorusKilogramsDryMatter=0,
                CarbonToNitrogenRatio=12,
                MoistureContent=0
            ),
            Bedding.get_bedding_material_composition(
                animal_type=AnimalType.dairy,
                bedding_material_type=BeddingMaterialType.separated_manure_solid.value))

    def test_get_bedding_material_composition_for_dairy_and_straw_long_returns_expected_results(self):
        self.assertEqual(
            dict(
                AnimalType=AnimalType.dairy.value,
                BeddingMaterial=BeddingMaterialType.straw_long.value,
                TotalNitrogenKilogramsDryMatter=0.0057,
                TotalCarbonKilogramsDryMatter=0.447,
                TotalPhosphorusKilogramsDryMatter=0.000635,
                CarbonToNitrogenRatio=90.5,
                MoistureContent=9.57
            ),
            Bedding.get_bedding_material_composition(
                animal_type=AnimalType.dairy,
                bedding_material_type=BeddingMaterialType.straw_long.value))

    def test_get_bedding_material_composition_for_dairy_and_straw_chopped_returns_expected_results(self):
        self.assertEqual(
            dict(
                AnimalType=AnimalType.dairy.value,
                BeddingMaterial=BeddingMaterialType.straw_chopped.value,
                TotalNitrogenKilogramsDryMatter=0.0057,
                TotalCarbonKilogramsDryMatter=0.447,
                TotalPhosphorusKilogramsDryMatter=0.000635,
                CarbonToNitrogenRatio=90.5,
                MoistureContent=9.57
            ),
            Bedding.get_bedding_material_composition(
                animal_type=AnimalType.dairy,
                bedding_material_type=BeddingMaterialType.straw_chopped.value))

    def test_get_bedding_material_composition_for_dairy_and_shavings_returns_expected_results(self):
        self.assertEqual(
            dict(
                AnimalType=AnimalType.dairy.value,
                BeddingMaterial=BeddingMaterialType.shavings.value,
                TotalNitrogenKilogramsDryMatter=0.00185,
                TotalCarbonKilogramsDryMatter=0.506,
                TotalPhosphorusKilogramsDryMatter=0.000275,
                CarbonToNitrogenRatio=329.5,
                MoistureContent=10.09
            ),
            Bedding.get_bedding_material_composition(
                animal_type=AnimalType.dairy,
                bedding_material_type=BeddingMaterialType.shavings.value))

    def test_get_bedding_material_composition_for_dairy_and_sawdust_returns_expected_results(self):
        self.assertEqual(
            dict(
                AnimalType=AnimalType.dairy.value,
                BeddingMaterial=BeddingMaterialType.sawdust.value,
                TotalNitrogenKilogramsDryMatter=0.00185,
                TotalCarbonKilogramsDryMatter=0.506,
                TotalPhosphorusKilogramsDryMatter=0.000275,
                CarbonToNitrogenRatio=329.5,
                MoistureContent=10.99
            ),
            Bedding.get_bedding_material_composition(
                animal_type=AnimalType.dairy,
                bedding_material_type=BeddingMaterialType.sawdust.value))

    def test_get_bedding_material_composition_for_swine_and_straw_long_returns_expected_results(self):
        self.assertEqual(
            dict(
                AnimalType=AnimalType.swine.value,
                BeddingMaterial=BeddingMaterialType.straw_long.value,
                TotalNitrogenKilogramsDryMatter=0.0057,
                TotalCarbonKilogramsDryMatter=0.447,
                TotalPhosphorusKilogramsDryMatter=0.000635,
                CarbonToNitrogenRatio=90.5,
                MoistureContent=9.57
            ),
            Bedding.get_bedding_material_composition(
                animal_type=AnimalType.swine,
                bedding_material_type=BeddingMaterialType.straw_long.value))

    def test_get_bedding_material_composition_for_swine_and_straw_chopped_returns_expected_results(self):
        self.assertEqual(
            dict(
                AnimalType=AnimalType.swine.value,
                BeddingMaterial=BeddingMaterialType.straw_chopped.value,
                TotalNitrogenKilogramsDryMatter=0.0057,
                TotalCarbonKilogramsDryMatter=0.447,
                TotalPhosphorusKilogramsDryMatter=0.000635,
                CarbonToNitrogenRatio=90.5,
                MoistureContent=9.57
            ),
            Bedding.get_bedding_material_composition(
                animal_type=AnimalType.swine,
                bedding_material_type=BeddingMaterialType.straw_chopped.value))

    def test_get_bedding_material_composition_for_sheep_and_straw_returns_expected_results(self):
        self.assertEqual(
            dict(
                AnimalType=AnimalType.sheep.value,
                BeddingMaterial=BeddingMaterialType.straw.value,
                TotalNitrogenKilogramsDryMatter=0.0057,
                TotalCarbonKilogramsDryMatter=0.447,
                TotalPhosphorusKilogramsDryMatter=0.000635,
                CarbonToNitrogenRatio=90.5,
                MoistureContent=9.57
            ),
            Bedding.get_bedding_material_composition(
                animal_type=AnimalType.sheep,
                bedding_material_type=BeddingMaterialType.straw.value))

    def test_get_bedding_material_composition_for_sheep_and_shavings_returns_expected_results(self):
        self.assertEqual(
            dict(
                AnimalType=AnimalType.sheep.value,
                BeddingMaterial=BeddingMaterialType.shavings.value,
                TotalNitrogenKilogramsDryMatter=0.00185,
                TotalCarbonKilogramsDryMatter=0.506,
                TotalPhosphorusKilogramsDryMatter=0.000275,
                CarbonToNitrogenRatio=329.5,
                MoistureContent=10.09
            ),
            Bedding.get_bedding_material_composition(
                animal_type=AnimalType.sheep,
                bedding_material_type=BeddingMaterialType.shavings.value))

    def test_get_bedding_material_composition_for_poultry_and_straw_returns_expected_results(self):
        self.assertEqual(
            dict(
                AnimalType=AnimalType.poultry.value,
                BeddingMaterial=BeddingMaterialType.straw.value,
                TotalNitrogenKilogramsDryMatter=0.0057,
                TotalCarbonKilogramsDryMatter=0.447,
                TotalPhosphorusKilogramsDryMatter=0.000635,
                CarbonToNitrogenRatio=90.5,
                MoistureContent=9.57
            ),
            Bedding.get_bedding_material_composition(
                animal_type=AnimalType.poultry,
                bedding_material_type=BeddingMaterialType.straw.value))

    def test_get_bedding_material_composition_for_poultry_and_shavings_returns_expected_results(self):
        self.assertEqual(
            dict(
                AnimalType=AnimalType.poultry.value,
                BeddingMaterial=BeddingMaterialType.shavings.value,
                TotalNitrogenKilogramsDryMatter=0.00185,
                TotalCarbonKilogramsDryMatter=0.506,
                TotalPhosphorusKilogramsDryMatter=0.000275,
                CarbonToNitrogenRatio=329.5,
                MoistureContent=10.09
            ),
            Bedding.get_bedding_material_composition(
                animal_type=AnimalType.poultry,
                bedding_material_type=BeddingMaterialType.shavings.value))

    def test_get_bedding_material_composition_for_poultry_and_sawdust_returns_expected_results(self):
        self.assertEqual(
            dict(
                AnimalType=AnimalType.poultry.value,
                BeddingMaterial=BeddingMaterialType.sawdust.value,
                TotalNitrogenKilogramsDryMatter=0.00185,
                TotalCarbonKilogramsDryMatter=0.506,
                TotalPhosphorusKilogramsDryMatter=0.000275,
                CarbonToNitrogenRatio=329.5,
                MoistureContent=10.99
            ),
            Bedding.get_bedding_material_composition(
                animal_type=AnimalType.poultry,
                bedding_material_type=BeddingMaterialType.sawdust.value))

    def test_get_bedding_material_composition_for_llamas_and_straw_returns_expected_results(self):
        self.assertEqual(
            dict(
                AnimalType=AnimalType.llamas.value,
                BeddingMaterial=BeddingMaterialType.straw.value,
                MoistureContent=9.57,
                TotalNitrogenKilogramsDryMatter=0.0057,
                TotalCarbonKilogramsDryMatter=0.447,
                TotalPhosphorusKilogramsDryMatter=0.000635,
                CarbonToNitrogenRatio=90.5
            ),
            Bedding.get_bedding_material_composition(
                animal_type=AnimalType.llamas,
                bedding_material_type=BeddingMaterialType.straw.value))

    def test_get_bedding_material_composition_for_alpacas_and_straw_returns_expected_results(self):
        self.assertEqual(
            dict(
                AnimalType=AnimalType.alpacas.value,
                BeddingMaterial=BeddingMaterialType.straw.value,
                MoistureContent=9.57,
                TotalNitrogenKilogramsDryMatter=0.0057,
                TotalCarbonKilogramsDryMatter=0.447,
                TotalPhosphorusKilogramsDryMatter=0.000635,
                CarbonToNitrogenRatio=90.5
            ),
            Bedding.get_bedding_material_composition(
                animal_type=AnimalType.alpacas,
                bedding_material_type=BeddingMaterialType.straw.value))

    def test_get_bedding_material_composition_for_deer_and_straw_returns_expected_results(self):
        self.assertEqual(
            dict(
                AnimalType=AnimalType.deer.value,
                BeddingMaterial=BeddingMaterialType.straw.value,
                MoistureContent=9.57,
                TotalNitrogenKilogramsDryMatter=0.0057,
                TotalCarbonKilogramsDryMatter=0.447,
                TotalPhosphorusKilogramsDryMatter=0.000635,
                CarbonToNitrogenRatio=90.5
            ),
            Bedding.get_bedding_material_composition(
                animal_type=AnimalType.deer,
                bedding_material_type=BeddingMaterialType.straw.value))

    def test_get_bedding_material_composition_for_elk_and_straw_returns_expected_results(self):
        self.assertEqual(
            dict(
                AnimalType=AnimalType.elk.value,
                BeddingMaterial=BeddingMaterialType.straw.value,
                MoistureContent=9.57,
                TotalNitrogenKilogramsDryMatter=0.0057,
                TotalCarbonKilogramsDryMatter=0.447,
                TotalPhosphorusKilogramsDryMatter=0.000635,
                CarbonToNitrogenRatio=90.5
            ),
            Bedding.get_bedding_material_composition(
                animal_type=AnimalType.elk,
                bedding_material_type=BeddingMaterialType.straw.value))

    def test_get_bedding_material_composition_for_goats_and_straw_returns_expected_results(self):
        self.assertEqual(
            dict(
                AnimalType=AnimalType.goats.value,
                BeddingMaterial=BeddingMaterialType.straw.value,
                MoistureContent=9.57,
                TotalNitrogenKilogramsDryMatter=0.0057,
                TotalCarbonKilogramsDryMatter=0.447,
                TotalPhosphorusKilogramsDryMatter=0.000635,
                CarbonToNitrogenRatio=90.5
            ),
            Bedding.get_bedding_material_composition(
                animal_type=AnimalType.goats,
                bedding_material_type=BeddingMaterialType.straw.value))

    def test_get_bedding_material_composition_for_horses_and_straw_returns_expected_results(self):
        self.assertEqual(
            dict(
                AnimalType=AnimalType.horses.value,
                BeddingMaterial=BeddingMaterialType.straw.value,
                MoistureContent=9.57,
                TotalNitrogenKilogramsDryMatter=0.0057,
                TotalCarbonKilogramsDryMatter=0.447,
                TotalPhosphorusKilogramsDryMatter=0.000635,
                CarbonToNitrogenRatio=90.5
            ),
            Bedding.get_bedding_material_composition(
                animal_type=AnimalType.horses,
                bedding_material_type=BeddingMaterialType.straw.value))

    def test_get_bedding_material_composition_for_mules_and_straw_returns_expected_results(self):
        self.assertEqual(
            dict(
                AnimalType=AnimalType.mules.value,
                BeddingMaterial=BeddingMaterialType.straw.value,
                MoistureContent=9.57,
                TotalNitrogenKilogramsDryMatter=0.0057,
                TotalCarbonKilogramsDryMatter=0.447,
                TotalPhosphorusKilogramsDryMatter=0.000635,
                CarbonToNitrogenRatio=90.5
            ),
            Bedding.get_bedding_material_composition(
                animal_type=AnimalType.mules,
                bedding_material_type=BeddingMaterialType.straw.value))

    def test_get_bedding_material_composition_for_bison_and_straw_returns_expected_results(self):
        self.assertEqual(
            dict(
                AnimalType=AnimalType.bison.value,
                BeddingMaterial=BeddingMaterialType.straw.value,
                MoistureContent=9.57,
                TotalNitrogenKilogramsDryMatter=0.0057,
                TotalCarbonKilogramsDryMatter=0.447,
                TotalPhosphorusKilogramsDryMatter=0.000635,
                CarbonToNitrogenRatio=90.5
            ),
            Bedding.get_bedding_material_composition(
                animal_type=AnimalType.bison,
                bedding_material_type=BeddingMaterialType.straw.value))


class TestGetMethaneProducingCapacityOfManure(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.animal_types = list(AnimalType)

    def run_test(
            self,
            animal_type: AnimalType,
            expected_value: float
    ):
        self.assertEqual(
            expected_value,
            get_methane_producing_capacity_of_manure(animal_type=animal_type))

        self.animal_types.pop(self.animal_types.index(animal_type))
        pass

    def test_get_methane_producing_capacity_of_manure_returns_expected_values_when_is_beef_cattle_type(self):
        for animal_type in [
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
            common.AnimalType.beef_cow_dry
        ]:
            self.run_test(animal_type=animal_type, expected_value=0.19)

    def test_get_methane_producing_capacity_of_manure_returns_expected_values_when_is_dairy_cattle_type(self):
        for animal_type in [
            common.AnimalType.dairy,
            common.AnimalType.dairy_lactating_cow,
            common.AnimalType.dairy_bulls,
            common.AnimalType.dairy_calves,
            common.AnimalType.dairy_dry_cow,
            common.AnimalType.dairy_heifers
        ]:
            self.run_test(animal_type=animal_type, expected_value=0.24)

    def test_get_methane_producing_capacity_of_manure_returns_expected_values_when_is_swine_type(self):
        for animal_type in [
            common.AnimalType.swine,
            common.AnimalType.swine_finisher,
            common.AnimalType.swine_starter,
            common.AnimalType.swine_lactating_sow,
            common.AnimalType.swine_dry_sow,
            common.AnimalType.swine_grower,
            common.AnimalType.swine_sows,
            common.AnimalType.swine_boar,
            common.AnimalType.swine_gilts,
            common.AnimalType.swine_piglets
        ]:
            self.run_test(animal_type=animal_type, expected_value=0.48)

    def test_get_methane_producing_capacity_of_manure_returns_expected_values_when_is_sheep_type(self):
        for animal_type in [
            common.AnimalType.sheep,
            common.AnimalType.lambs_and_ewes,
            common.AnimalType.ram,
            common.AnimalType.weaned_lamb,
            common.AnimalType.lambs,
            common.AnimalType.ewes,
            common.AnimalType.sheep_feedlot
        ]:
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
        for animal_type in self.animal_types:
            self.run_test(animal_type=animal_type, expected_value=0)


class TestGetDefaultMethaneProducingCapacityOfManure(unittest.TestCase):
    def test_get_default_methane_producing_capacity_of_manure_is_constant_for_pasture(self):
        for animal_type in common.AnimalType:
            self.assertEqual(
                0.19,
                get_default_methane_producing_capacity_of_manure(is_pasture=True, animal_type=animal_type))


if __name__ == '__main__':
    unittest.main()
