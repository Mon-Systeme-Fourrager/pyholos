import random
import unittest

from holos_service.components.land_management.crop import (CropType, get_valid_crop_types,
                                                           get_valid_perennial_types,
                                                           get_alberta_economic_crop_types,
                                                           get_saskatchewan_economic_crop_types,
                                                           get_manitoba_economic_crop_types,
                                                           get_ontario_economic_crop_types, get_grassland_types,
                                                           get_economic_crop_types)
from holos_service.utils import concat_lists


class _CropType:
    perennial = [
        CropType.Forage,
        CropType.TameGrass,
        CropType.TameLegume,
        CropType.TameMixed,
        CropType.PerennialForages,
        CropType.ForageForSeed,
        CropType.SeededGrassland,
        CropType.RangelandNative
    ]
    grassland = [
        CropType.BrokenGrassland,
        CropType.GrasslandSeeded,
        CropType.RangelandNative
    ]
    cover_crop = [
        CropType.RedCloverTrifoliumPratenseL,
        CropType.BerseemCloverTrifoliumAlexandriumL,
        CropType.SweetCloverMelilotusOfficinalis,
        CropType.CrimsonCloverTrifoliumIncarnatum,
        CropType.HairyVetchViciaVillosaRoth,
        CropType.AlfalfaMedicagoSativaL,
        CropType.FabaBeanBroadBeanViciaFaba,
        CropType.CowpeaVignaUnguiculata,
        CropType.AustrianWinterPea,
        CropType.RapeseedBrassicaNapusL,
        CropType.WinterTurnipRapeBrassicaRapaSppOleiferaLCVLargo,
        CropType.PhaceliaPhaceliaTanacetifoliaCVPhaci,
        CropType.ForageRadishRaphanusSativusL,
        CropType.MustardSinapusAlbaLSubspMaireiHLindbMaire,
        CropType.BarleyHordeumVulgare,
        CropType.OatAvenaSativa,
        CropType.RyeSecaleCerealeWinterRyeCerealRye,
        CropType.SesameSesamumIndicum,
        CropType.FlaxLinumUsitatissimum,
        CropType.RyeGrassLoliumPerenneL,
        CropType.AnnualRyeGrassLoliumMultiflorum,
        CropType.SorghumSorghumBicolour,
        CropType.PigeonBean,
        CropType.ShepherdsPurse,
        CropType.WinterWheatTriticumAestivum
    ]
    leguminous_cover_crop = [
        CropType.RedCloverTrifoliumPratenseL,
        CropType.BerseemCloverTrifoliumAlexandriumL,
        CropType.SweetCloverMelilotusOfficinalis,
        CropType.CrimsonCloverTrifoliumIncarnatum,
        CropType.HairyVetch,
        CropType.AlfalfaMedicagoSativaL,
        CropType.FabaBeanBroadBeanViciaFaba,
        CropType.CowpeaVignaUnguiculata,
        CropType.AustrianWinterPea,
        CropType.PigeonBean
    ]
    non_leguminous_cover_crop = [
        CropType.WinterWeeds,
        CropType.RapeseedBrassicaNapusL,
        CropType.WinterTurnipRapeBrassicaRapaSppOleiferaLCVLargo,
        CropType.PhaceliaPhaceliaTanacetifoliaCVPhaci,
        CropType.ForageRadishRaphanusSativusL,
        CropType.MustardSinapusAlbaLSubspMaireiHLindbMaire,
        CropType.BarleyHordeumVulgare,
        CropType.OatAvenaSativa,
        CropType.RyeSecaleCerealeWinterRyeCerealRye,
        CropType.SesameSesamumIndicum,
        CropType.FlaxLinumUsitatissimum,
        CropType.RyeGrassLoliumPerenneL,
        CropType.AnnualRyeGrassLoliumMultiflorum,
        CropType.SorghumSorghumBicolour,
        CropType.WinterWheatTriticumAestivum,
        CropType.FallRye
    ]
    native_grassland = CropType.RangelandNative
    fallow = [
        CropType.Fallow,
        CropType.SummerFallow
    ]
    annual = [
        CropType.SmallGrainCereals,
        CropType.Wheat,
        CropType.WheatSilage,
        CropType.Barley,
        CropType.BarleySilage,
        CropType.UndersownBarley,
        CropType.Oats,
        CropType.OatSilage,
        CropType.Camelina,
        CropType.Triticale,
        CropType.TriticaleSilage,
        CropType.Sorghum,
        CropType.CanarySeed,
        CropType.Buckwheat,
        CropType.FallRye,
        CropType.MixedGrains,
        CropType.Oilseeds,
        CropType.Canola,
        CropType.Mustard,
        CropType.Flax,
        CropType.PulseCrops,
        CropType.Soybeans,
        CropType.BeansDryField,
        CropType.Chickpeas,
        CropType.DryPeas,
        CropType.FieldPeas,
        CropType.Lentils,
        CropType.GrainCorn,
        CropType.SilageCorn,
        CropType.Safflower,
        CropType.SunflowerSeed,
        CropType.Tobacco,
        CropType.Vegetables,
        CropType.BerriesAndGrapes,
        CropType.OtherFieldCrops
    ]
    silage_crop = [
        CropType.SilageCorn,
        CropType.GrassSilage,
        CropType.BarleySilage,
        CropType.OatSilage,
        CropType.TriticaleSilage,
        CropType.WheatSilage
    ]
    silage_crop_without_defaults = [
        CropType.BarleySilage,
        CropType.OatSilage,
        CropType.SilageCorn,
        CropType.TriticaleSilage,
        CropType.GrassSilage,
        CropType.WheatSilage
    ]
    root_crops = [
        CropType.Potatoes,
        CropType.SugarBeets
    ]
    small_grains = [
        CropType.SmallGrainCereals,
        CropType.Wheat,
        CropType.WinterWheat,
        CropType.WheatSilage,
        CropType.Barley,
        CropType.GrainCorn,
        CropType.BarleySilage,
        CropType.UndersownBarley,
        CropType.Oats,
        CropType.OatSilage,
        CropType.Triticale,
        CropType.TriticaleSilage,
        CropType.Sorghum,
        CropType.CanarySeed,
        CropType.Buckwheat,
        CropType.FallRye,
        CropType.MixedGrains
    ]
    oil_seed = [
        CropType.Oilseeds,
        CropType.Canola,
        CropType.Camelina,
        CropType.Mustard,
        CropType.Soybeans,
        CropType.Flax
    ]
    other_field_crop = [
        CropType.Safflower,
        CropType.SunflowerSeed,
        CropType.Tobacco,
        CropType.Vegetables,
        CropType.BerriesAndGrapes,
        CropType.OtherFieldCrops
    ]
    pulse_crop = [
        CropType.PulseCrops,
        CropType.BeansDryField,
        CropType.Chickpeas,
        CropType.DryPeas,
        CropType.FieldPeas,
        CropType.Lentils
    ]
    national_inventory_report = [
        CropType.Barley,
        CropType.Buckwheat,
        CropType.Canola,
        CropType.SmallGrainCereals,
        CropType.Chickpeas,
        CropType.GrainCorn,
        CropType.SilageCorn,
        CropType.BeansDryField,
        CropType.FieldPeas,
        CropType.FabaBeans,
        CropType.FlaxSeed,
        CropType.Grains,
        CropType.Lentils,
        CropType.MustardSeed,
        CropType.MixedGrains,
        CropType.Oats,
        CropType.OtherDryFieldBeans,
        CropType.Oilseeds,
        CropType.Peas,
        CropType.Potatoes,
        CropType.Pulses,
        CropType.Rye,
        CropType.FallRye,
        CropType.SpringRye,
        CropType.Safflower,
        CropType.Soybeans,
        CropType.SugarBeets,
        CropType.SunflowerSeed,
        CropType.Triticale,
        CropType.WhiteBeans,
        CropType.Wheat,
        CropType.WheatRye,
        CropType.SpringWheat,
        CropType.WinterWheat,
        CropType.Durum,
        CropType.CanarySeed,
        CropType.Tobacco
    ]

    valid_crop_types = [
        CropType.Barley,
        CropType.BarleySilage,
        CropType.BeansDryField,
        CropType.BerriesAndGrapes,
        CropType.Buckwheat,
        CropType.CanarySeed,
        CropType.Canola,
        CropType.Chickpeas,
        CropType.Camelina,
        CropType.DryPeas,
        CropType.FallRye,
        CropType.Flax,
        CropType.ForageForSeed,
        CropType.GrainCorn,
        CropType.GrassSilage,
        CropType.TameGrass,
        CropType.TameLegume,
        CropType.TameMixed,
        CropType.Lentils,
        CropType.MixedGrains,
        CropType.Mustard,
        CropType.OatSilage,
        CropType.Oats,
        CropType.Oilseeds,
        CropType.RangelandNative,
        CropType.OtherFieldCrops,
        CropType.SeededGrassland,
        CropType.Potatoes,
        CropType.PulseCrops,
        CropType.Safflower,
        CropType.SilageCorn,
        CropType.SmallGrainCereals,
        CropType.Sorghum,
        CropType.Soybeans,
        CropType.SugarBeets,
        CropType.SummerFallow,
        CropType.SunflowerSeed,
        CropType.Tobacco,
        CropType.Triticale,
        CropType.TriticaleSilage,
        CropType.UndersownBarley,
        CropType.Vegetables,
        CropType.Wheat,
        CropType.WheatSilage
    ]
    valid_perennial_types = [
        CropType.ForageForSeed,
        CropType.TameGrass,
        CropType.TameLegume,
        CropType.TameMixed,
        CropType.RangelandNative,
        CropType.SeededGrassland
    ]


class _EconomicCropTypes:
    alberta = [
        CropType.AlfalfaHay,
        CropType.ArgentineHTCanola,
        CropType.CPSWheat,
        CropType.CerealSilage,
        CropType.DryBean,
        CropType.Durum,
        CropType.FeedBarley,
        CropType.FieldPeas,
        CropType.Flax,
        CropType.TameMixed,
        CropType.KabuliChickpea,
        CropType.MaltBarley,
        CropType.MillingOats,
        CropType.PolishCanola,
        CropType.RedLentils,
        CropType.SoftWheat,
        CropType.SpringWheat,
        CropType.SummerFallow,
        CropType.YellowMustard
    ]
    saskatchewan = [
        CropType.BlackBean,
        CropType.BrownMustard,
        CropType.Camelina,
        CropType.CanarySeed,
        CropType.Canola,
        CropType.CarawayFirstSeason,
        CropType.CarawaySecondSeason,
        CropType.Coriander,
        CropType.Corn,
        CropType.DesiChickpeas,
        CropType.Durum,
        CropType.EdibleGreenPeas,
        CropType.EdibleYellowPeas,
        CropType.FabaBeans,
        CropType.FeedBarley,
        CropType.Fenugreek,
        CropType.Flax,
        CropType.HybridFallRye,
        CropType.LargeGreenLentils,
        CropType.LargeKabuliChickpea,
        CropType.MaltBarley,
        CropType.Oats,
        CropType.OrientalMustard,
        CropType.Quinoa,
        CropType.RedLentils,
        CropType.SmallKabuliChickpea,
        CropType.Soybeans,
        CropType.SpringWheat,
        CropType.SunflowerOilseedEMSS,
        CropType.WinterWheat,
        CropType.YellowMustard
    ]
    manitoba = [
        CropType.Barley,
        CropType.BeansPinto,
        CropType.BeansWhite,
        CropType.Canola,
        CropType.Corn,
        CropType.FlaxSeed,
        CropType.HardRedSpringWheat,
        CropType.HybridFallRye,
        CropType.Oats,
        CropType.Peas,
        CropType.Soybeans,
        CropType.SunflowerConfection,
        CropType.SunflowerOil,
        CropType.WheatNorthernHardRed,
        CropType.WheatOtherSpring,
        CropType.WheatPrairieSpring,
        CropType.WinterWheat
    ]
    ontario = [
        CropType.AlfalfaHay,
        CropType.ColouredBeans,
        CropType.CornSilage,
        CropType.GrainCorn,
        CropType.HardRedSpringWheat,
        CropType.HardRedWinterWheat,
        CropType.HardRedWinterWheatNoTill,
        CropType.NorthernOntarioBarley,
        CropType.NorthernOntarioOats,
        CropType.SoftWinterWheat,
        CropType.SoftWinterWheatNoTill,
        CropType.SouthernOntarioBarley,
        CropType.SouthernOntarioOats,
        CropType.SoybeanNoTill,
        CropType.Soybeans,
        CropType.SoybeansRoundUpReady,
        CropType.SpringCanolaHt,
        CropType.SwitchgrassDirect,
        CropType.SwitchgrassDirectNoTill,
        CropType.SwitchgrassUnderseeded,
        CropType.SwitchgrassUnderseededNoTill,
        CropType.WhiteBlackBeans,
        CropType.WinterCanolaHybrid
    ]


class TestCropTypeExtension(unittest.TestCase):
    def test_is_perennial(self):
        for crop_type in _CropType.perennial:
            self.assertTrue(
                crop_type.is_perennial())

    def test_is_pasture(self):
        for crop_type in concat_lists(_CropType.perennial, _CropType.grassland):
            self.assertTrue(
                crop_type.is_pasture())

    def test_is_cover_crop(self):
        for crop_type in _CropType.cover_crop:
            self.assertTrue(
                crop_type.is_cover_crop())

    def test_is_leguminous_cover_crop(self):
        for crop_type in _CropType.leguminous_cover_crop:
            self.assertTrue(
                crop_type.is_leguminous_cover_crop())

    def test_is_non_leguminous_cover_crop(self):
        for crop_type in _CropType.non_leguminous_cover_crop:
            self.assertTrue(
                crop_type.is_non_leguminous_cover_crop())

    def test_is_rangeland(self):
        self.assertTrue(random.choice(list(CropType)))

    def test_is_grassland(self):
        for crop_type in _CropType.grassland:
            self.assertTrue(
                crop_type.is_grassland())

    def test_is_native_grassland(self):
        self.assertTrue(_CropType.native_grassland.is_native_grassland())

    def test_is_fallow(self):
        for crop_type in _CropType.fallow:
            self.assertTrue(
                crop_type.is_fallow())

    def test_is_annual(self):
        for crop_type in concat_lists(_CropType.silage_crop, _CropType.root_crops, _CropType.annual):
            self.assertTrue(
                crop_type.is_annual())

    def test_is_silage_crop(self):
        for crop_type in _CropType.silage_crop:
            self.assertTrue(
                crop_type.is_silage_crop())

    def test_is_silage_crop_without_defaults(self):
        for crop_type in _CropType.silage_crop:
            self.assertTrue(
                crop_type.is_silage_crop_without_defaults())

    def test_get_grain_crop_equivalent_of_silage_crop(self):
        crop_types = []
        for crop_type, grain_crop_equivalent in [
            (CropType.BarleySilage, CropType.Barley),
            (CropType.OatSilage, CropType.Oats),
            (CropType.GrassSilage, CropType.TameLegume),
            (CropType.TriticaleSilage, CropType.Triticale),
            (CropType.WheatSilage, CropType.Wheat),
            (CropType.CornSilage, CropType.GrainCorn),
            (CropType.SilageCorn, CropType.GrainCorn),
            (CropType.CerealSilage, CropType.Cereals)
        ]:
            self.assertEqual(
                grain_crop_equivalent,
                crop_type.get_grain_crop_equivalent_of_silage_crop()
            )
            crop_types.append(crop_type)

        for crop in CropType:
            if crop not in crop_types:
                self.assertIsNone(
                    crop.get_grain_crop_equivalent_of_silage_crop()
                )

    def test_is_root_crop(self):
        for crop_type in _CropType.root_crops:
            self.assertTrue(
                crop_type.is_root_crop())

    def test_is_small_grains(self):
        for crop_type in _CropType.small_grains:
            self.assertTrue(
                crop_type.is_small_grains())

    def test_is_oil_seed(self):
        for crop_type in _CropType.oil_seed:
            self.assertTrue(
                crop_type.is_oil_seed())

    def test_is_other_field_crop(self):
        for crop_type in _CropType.other_field_crop:
            self.assertTrue(
                crop_type.is_other_field_crop())

    def test_is_pulse_crop(self):
        for crop_type in _CropType.pulse_crop:
            self.assertTrue(
                crop_type.is_pulse_crop())

    def test_is_economic_crop(self):
        self.assertEqual(
            sorted(
                concat_lists(_EconomicCropTypes.alberta,
                             _EconomicCropTypes.manitoba,
                             _EconomicCropTypes.ontario,
                             _EconomicCropTypes.saskatchewan,
                             )),
            get_economic_crop_types()
        )

    def test_national_inventory_report(self):
        for crop_type in _CropType.national_inventory_report:
            self.assertTrue(
                crop_type.is_national_inventory_report())

    def test_valid_crop_types(self):
        self.assertEqual(
            sorted(_CropType.valid_crop_types),
            get_valid_crop_types()
        )

    def test_valid_perennial_types(self):
        self.assertEqual(
            sorted(_CropType.valid_perennial_types),
            get_valid_perennial_types()
        )

    def test_alberta_economic_crop_types(self):
        self.assertEqual(
            sorted(_EconomicCropTypes.alberta),
            get_alberta_economic_crop_types()
        )

    def test_saskatchewan_economic_crop_types(self):
        self.assertEqual(
            sorted(_EconomicCropTypes.saskatchewan),
            get_saskatchewan_economic_crop_types()
        )

    def test_manitoba_economic_crop_types(self):
        self.assertEqual(
            sorted(_EconomicCropTypes.manitoba),
            get_manitoba_economic_crop_types()
        )

    def test_ontario_economic_crop_types(self):
        self.assertEqual(
            sorted(_EconomicCropTypes.ontario),
            get_ontario_economic_crop_types()
        )

    def test_get_grassland_types(self):
        grassland_types = _CropType.grassland
        grassland_types.pop(grassland_types.index(CropType.RangelandNative))
        self.assertEqual(
            grassland_types,
            get_grassland_types()
        )


if __name__ == '__main__':
    unittest.main()
