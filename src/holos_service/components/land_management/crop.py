from enum import auto

from holos_service.utils import AutoNameEnum, concat_lists


class CropType(AutoNameEnum):
    """
    Holos Source Code:
        - CropType members: https://github.com/holos-aafc/Holos/blob/c5b1a960639be5c4fa6a25e167c49c36403c291d/H.Core/Enumerations/CropType.cs#L5
        - CropType extension methods: https://github.com/holos-aafc/Holos/blob/c5b1a960639be5c4fa6a25e167c49c36403c291d/H.Core/Enumerations/CropTypeExtensions.cs#L15

    """
    AlfalfaMedicagoSativaL = auto()
    AlfalfaSeed = auto()
    AnnualRyeGrassLoliumMultiflorum = auto()
    AustrianWinterPea = auto()
    Barley = auto()
    BarleyHordeumVulgare = auto()
    BarleySilage = auto()
    BarleySilageUnderSeed = auto()
    BeansDryField = auto()
    BerriesAndGrapes = auto()
    BerseemCloverTrifoliumAlexandriumL = auto()
    BrokenGrassland = auto()
    BromeHay = auto()
    Buckwheat = auto()
    CanarySeed = auto()
    Canola = auto()
    Caraway = auto()
    Carrot = auto()
    Chickpeas = auto()
    ColouredWhiteFabaBeans = auto()
    Corn = auto()
    CornSilage = auto()
    CowpeaVignaUnguiculata = auto()
    CPSWheat = auto()
    CrimsonCloverTrifoliumIncarnatum = auto()
    Dill = auto()
    DryBean = auto()
    DryPeas = auto()
    Durum = auto()
    FabaBeanBroadBeanViciaFaba = auto()
    FabaBeans = auto()
    Fallow = auto()
    FallRye = auto()
    FieldPeas = auto()
    Flax = auto()
    FlaxLinumUsitatissimum = auto()
    FlaxSeed = auto()
    FodderCorn = auto()
    Forage = auto()
    ForageForSeed = auto()
    ForageRadishRaphanusSativusL = auto()
    FreshCornSweet = auto()
    FreshPeas = auto()
    GrainCorn = auto()
    GrainSorghum = auto()
    GrassHay = auto()
    GrasslandSeeded = auto()
    GrassSeed = auto()
    GreenFeed = auto()
    HairyVetch = auto()
    HairyVetchAndRye = auto()
    HairyVetchViciaVillosaRoth = auto()
    HardRedSpringWheat = auto()
    HayAndForageSeed = auto()
    Hyola = auto()
    Lentils = auto()
    Linola = auto()
    MaltBarley = auto()
    MarketGarden = auto()
    MilkVetch = auto()
    Millet = auto()
    Mint = auto()
    MixedGrains = auto()
    Monarda = auto()
    Mustard = auto()
    MustardSeed = auto()
    MustardSinapusAlbaLSubspMaireiHLindbMaire = auto()
    NativePasture = auto()
    NotSelected = auto()
    OatAvenaSativa = auto()
    Oats = auto()
    OatSilage = auto()
    Oilseeds = auto()
    Onion = auto()
    OtherFieldCrops = auto()
    Peas = auto()
    PerennialForages = auto()
    PhaceliaPhaceliaTanacetifoliaCVPhaci = auto()
    PigeonBean = auto()
    Potatoes = auto()
    PulseCrops = auto()
    RangelandNative = auto()
    RapeseedBrassicaNapusL = auto()
    RedCloverTrifoliumPratenseL = auto()
    Rye = auto()
    RyeGrassLoliumPerenneL = auto()
    RyeSecaleCerealeWinterRyeCerealRye = auto()
    Safflower = auto()
    SeededGrassland = auto()
    SeedPotato = auto()
    SesameSesamumIndicum = auto()
    ShepherdsPurse = auto()
    SilageCorn = auto()
    SmallFruit = auto()
    SmallGrainCereals = auto()
    SoftWheat = auto()
    Sorghum = auto()
    SorghumSorghumBicolour = auto()
    SorghumSudanGrass = auto()
    Soybeans = auto()
    SpringRye = auto()
    SpringWheat = auto()
    SugarBeets = auto()
    SummerFallow = auto()
    Sunflower = auto()
    SunflowerSeed = auto()
    SweetCloverMelilotusOfficinalis = auto()
    TameGrass = auto()
    TameLegume = auto()
    TameMixed = auto()
    TamePasture = auto()
    TimothyHay = auto()
    Tobacco = auto()
    TreeFruitAndNuts = auto()
    Triticale = auto()
    TriticaleSilage = auto()
    TurfSod = auto()
    UndersownBarley = auto()
    Vegetables = auto()
    Wheat = auto()
    WheatBolinder = auto()
    WheatGan = auto()
    WheatSilage = auto()
    WinterTurnipRapeBrassicaRapaSppOleiferaLCVLargo = auto()
    WinterWeeds = auto()
    WinterWheat = auto()
    WinterWheatTriticumAestivum = auto()
    NONE = auto()

    # region Economic Crops
    AlfalfaHay = auto()
    ArgentineHTCanola = auto()
    BeansPinto = auto()
    BeansWhite = auto()
    BlackBean = auto()
    BrownMustard = auto()
    Camelina = auto()
    CarawayFirstSeason = auto()
    CarawaySecondSeason = auto()
    CerealSilage = auto()
    ColouredBeans = auto()
    Coriander = auto()
    DesiChickpeas = auto()
    EdibleGreenPeas = auto()
    EdibleYellowPeas = auto()
    FeedBarley = auto()
    Fenugreek = auto()
    HardRedWinterWheat = auto()
    HardRedWinterWheatNoTill = auto()
    HybridFallRye = auto()
    KabuliChickpea = auto()
    LargeGreenLentils = auto()
    LargeKabuliChickpea = auto()
    MillingOats = auto()
    NorthernOntarioBarley = auto()
    NorthernOntarioOats = auto()
    OrientalMustard = auto()
    PolishCanola = auto()
    Quinoa = auto()
    RedLentils = auto()
    SmallKabuliChickpea = auto()
    SoftWinterWheat = auto()
    SoftWinterWheatNoTill = auto()
    SouthernOntarioBarley = auto()
    SouthernOntarioOats = auto()
    SoybeanNoTill = auto()
    SoybeansRoundUpReady = auto()
    SpringCanolaHt = auto()
    SunflowerConfection = auto()
    SunflowerOil = auto()
    SunflowerOilseedEMSS = auto()
    SwitchgrassDirect = auto()
    SwitchgrassDirectNoTill = auto()
    SwitchgrassUnderseeded = auto()
    SwitchgrassUnderseededNoTill = auto()
    UserDefined = auto()
    WheatHardRedSpring = auto()
    WheatNorthernHardRed = auto()
    WheatOtherSpring = auto()
    WheatPrairieSpring = auto()
    WhiteBlackBeans = auto()
    WinterCanolaHybrid = auto()
    YellowMustard = auto()
    # endregion

    # Note from the original holos code:
    #   The new crops below are from the "Default values for nitrogen and lignin contents in crops for steady state methods.
    # region Nitrogen and lignin contents table
    Beans = auto()
    Cereals = auto()
    DryFieldPeas = auto()
    GenericGrains = auto()
    Grains = auto()
    GrassCloverMixtures = auto()
    NFixingForages = auto()
    NonLegumeHay = auto()
    NonNFixingForages = auto()
    OtherDryFieldBeans = auto()
    Peanuts = auto()
    PerennialGrasses = auto()
    Pulses = auto()
    Rice = auto()
    Tubers = auto()
    WheatRye = auto()
    WhiteBeans = auto()
    # endregion

    GrassSilage = auto()

    # extensions
    """https://github.com/holos-aafc/Holos/blob/c5b1a960639be5c4fa6a25e167c49c36403c291d/H.Core/Enumerations/CropTypeExtensions.cs#L15"""

    def is_perennial(self):
        return self in [
            self.__class__.Forage,
            self.__class__.TameGrass,
            self.__class__.TameLegume,
            self.__class__.TameMixed,
            self.__class__.PerennialForages,
            self.__class__.ForageForSeed,
            self.__class__.SeededGrassland,
            self.__class__.RangelandNative
        ]

    def is_pasture(self):
        return self.is_perennial() or self.is_grassland()

    def is_cover_crop(self):
        return [
            self.__class__.RedCloverTrifoliumPratenseL,
            self.__class__.BerseemCloverTrifoliumAlexandriumL,
            self.__class__.SweetCloverMelilotusOfficinalis,
            self.__class__.CrimsonCloverTrifoliumIncarnatum,
            self.__class__.HairyVetchViciaVillosaRoth,
            self.__class__.AlfalfaMedicagoSativaL,
            self.__class__.FabaBeanBroadBeanViciaFaba,
            self.__class__.CowpeaVignaUnguiculata,
            self.__class__.AustrianWinterPea,
            self.__class__.RapeseedBrassicaNapusL,
            self.__class__.WinterTurnipRapeBrassicaRapaSppOleiferaLCVLargo,
            self.__class__.PhaceliaPhaceliaTanacetifoliaCVPhaci,
            self.__class__.ForageRadishRaphanusSativusL,
            self.__class__.MustardSinapusAlbaLSubspMaireiHLindbMaire,
            self.__class__.BarleyHordeumVulgare,
            self.__class__.OatAvenaSativa,
            self.__class__.RyeSecaleCerealeWinterRyeCerealRye,
            self.__class__.SesameSesamumIndicum,
            self.__class__.FlaxLinumUsitatissimum,
            self.__class__.RyeGrassLoliumPerenneL,
            self.__class__.AnnualRyeGrassLoliumMultiflorum,
            self.__class__.SorghumSorghumBicolour,
            self.__class__.PigeonBean,
            self.__class__.ShepherdsPurse,
            self.__class__.WinterWheatTriticumAestivum
        ]

    def is_leguminous_cover_crop(self):
        return self in [
            self.__class__.RedCloverTrifoliumPratenseL,
            self.__class__.BerseemCloverTrifoliumAlexandriumL,
            self.__class__.SweetCloverMelilotusOfficinalis,
            self.__class__.CrimsonCloverTrifoliumIncarnatum,
            self.__class__.HairyVetch,
            self.__class__.AlfalfaMedicagoSativaL,
            self.__class__.FabaBeanBroadBeanViciaFaba,
            self.__class__.CowpeaVignaUnguiculata,
            self.__class__.AustrianWinterPea,
            self.__class__.PigeonBean
        ]

    def is_non_leguminous_cover_crop(self):
        return self in [
            self.__class__.WinterWeeds,
            self.__class__.RapeseedBrassicaNapusL,
            self.__class__.WinterTurnipRapeBrassicaRapaSppOleiferaLCVLargo,
            self.__class__.PhaceliaPhaceliaTanacetifoliaCVPhaci,
            self.__class__.ForageRadishRaphanusSativusL,
            self.__class__.MustardSinapusAlbaLSubspMaireiHLindbMaire,
            self.__class__.BarleyHordeumVulgare,
            self.__class__.OatAvenaSativa,
            self.__class__.RyeSecaleCerealeWinterRyeCerealRye,
            self.__class__.SesameSesamumIndicum,
            self.__class__.FlaxLinumUsitatissimum,
            self.__class__.RyeGrassLoliumPerenneL,
            self.__class__.AnnualRyeGrassLoliumMultiflorum,
            self.__class__.SorghumSorghumBicolour,
            self.__class__.WinterWheatTriticumAestivum,
            self.__class__.FallRye
        ]

    @staticmethod
    def is_rangeland():
        return False

    def is_grassland(self):
        return self in [
            self.__class__.BrokenGrassland,
            self.__class__.GrasslandSeeded,
            self.__class__.RangelandNative
        ]

    def is_native_grassland(self):
        return self == self.__class__.RangelandNative

    def is_fallow(self):
        return self in [
            self.__class__.Fallow,
            self.__class__.SummerFallow
        ]

    def is_annual(self):
        if self.is_silage_crop() or self.is_root_crop():
            return True
        else:
            return self in [
                self.__class__.SmallGrainCereals,
                self.__class__.Wheat,
                self.__class__.WheatSilage,
                self.__class__.Barley,
                self.__class__.BarleySilage,
                self.__class__.UndersownBarley,
                self.__class__.Oats,
                self.__class__.OatSilage,
                self.__class__.Camelina,
                self.__class__.Triticale,
                self.__class__.TriticaleSilage,
                self.__class__.Sorghum,
                self.__class__.CanarySeed,
                self.__class__.Buckwheat,
                self.__class__.FallRye,
                self.__class__.MixedGrains,
                self.__class__.Oilseeds,
                self.__class__.Canola,
                self.__class__.Mustard,
                self.__class__.Flax,
                self.__class__.PulseCrops,
                self.__class__.Soybeans,
                self.__class__.BeansDryField,
                self.__class__.Chickpeas,
                self.__class__.DryPeas,
                self.__class__.FieldPeas,
                self.__class__.Lentils,
                self.__class__.GrainCorn,
                self.__class__.SilageCorn,
                self.__class__.Safflower,
                self.__class__.SunflowerSeed,
                self.__class__.Tobacco,
                self.__class__.Vegetables,
                self.__class__.BerriesAndGrapes,
                self.__class__.OtherFieldCrops
            ]

    def is_silage_crop(self):
        return self in [
            self.__class__.SilageCorn,
            self.__class__.GrassSilage,
            self.__class__.BarleySilage,
            self.__class__.OatSilage,
            self.__class__.TriticaleSilage,
            self.__class__.WheatSilage
        ]

    def is_silage_crop_without_defaults(self):
        return self in [
            self.__class__.BarleySilage,
            self.__class__.OatSilage,
            self.__class__.SilageCorn,
            self.__class__.TriticaleSilage,
            self.__class__.GrassSilage,
            self.__class__.WheatSilage
        ]

    def get_grain_crop_equivalent_of_silage_crop(self):
        match self:
            case CropType.BarleySilage:
                return CropType.Barley
            case CropType.OatSilage:
                return CropType.Oats
            case CropType.GrassSilage:
                return CropType.TameLegume
            case CropType.TriticaleSilage:
                return CropType.Triticale
            case CropType.WheatSilage:
                return CropType.Wheat
            case CropType.CornSilage | CropType.SilageCorn:
                return CropType.GrainCorn
            case CropType.CerealSilage:
                return CropType.Cereals
            case _:
                return None

    def is_root_crop(self):
        return self in [
            self.__class__.Potatoes,
            self.__class__.SugarBeets,
        ]

    def is_small_grains(self):
        return self in [
            self.__class__.SmallGrainCereals,
            self.__class__.Wheat,
            self.__class__.WinterWheat,
            self.__class__.WheatSilage,
            self.__class__.Barley,
            self.__class__.GrainCorn,
            self.__class__.BarleySilage,
            self.__class__.UndersownBarley,
            self.__class__.Oats,
            self.__class__.OatSilage,
            self.__class__.Triticale,
            self.__class__.TriticaleSilage,
            self.__class__.Sorghum,
            self.__class__.CanarySeed,
            self.__class__.Buckwheat,
            self.__class__.FallRye,
            self.__class__.MixedGrains
        ]

    def is_oil_seed(self):
        return self in [
            self.__class__.Oilseeds,
            self.__class__.Canola,
            self.__class__.Camelina,
            self.__class__.Mustard,
            self.__class__.Soybeans,
            self.__class__.Flax
        ]

    def is_other_field_crop(self):
        return self in [
            self.__class__.Safflower,
            self.__class__.SunflowerSeed,
            self.__class__.Tobacco,
            self.__class__.Vegetables,
            self.__class__.BerriesAndGrapes,
            self.__class__.OtherFieldCrops
        ]

    def is_pulse_crop(self):
        return self in [
            self.__class__.PulseCrops,
            self.__class__.BeansDryField,
            self.__class__.Chickpeas,
            self.__class__.DryPeas,
            self.__class__.FieldPeas,
            self.__class__.Lentils
        ]

    def is_economic_type(self):
        return self in get_economic_crop_types()

    def is_national_inventory_report(self):
        return self in [
            self.__class__.Barley,
            self.__class__.Buckwheat,
            self.__class__.Canola,
            self.__class__.SmallGrainCereals,
            self.__class__.Chickpeas,
            self.__class__.GrainCorn,
            self.__class__.SilageCorn,
            self.__class__.BeansDryField,
            self.__class__.FieldPeas,
            self.__class__.FabaBeans,
            self.__class__.FlaxSeed,
            self.__class__.Grains,
            self.__class__.Lentils,
            self.__class__.MustardSeed,
            self.__class__.MixedGrains,
            self.__class__.Oats,
            self.__class__.OtherDryFieldBeans,
            self.__class__.Oilseeds,
            self.__class__.Peas,
            self.__class__.Potatoes,
            self.__class__.Pulses,
            self.__class__.Rye,
            self.__class__.FallRye,
            self.__class__.SpringRye,
            self.__class__.Safflower,
            self.__class__.Soybeans,
            self.__class__.SugarBeets,
            self.__class__.SunflowerSeed,
            self.__class__.Triticale,
            self.__class__.WhiteBeans,
            self.__class__.Wheat,
            self.__class__.WheatRye,
            self.__class__.SpringWheat,
            self.__class__.WinterWheat,
            self.__class__.Durum,
            self.__class__.CanarySeed,
            self.__class__.Tobacco,
        ]


def get_valid_cover_crop_types() -> list[None | CropType]:
    return [None] + sorted(
        [
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
    )


def get_economic_crop_types() -> list[CropType]:
    return sorted(concat_lists(
        get_alberta_economic_crop_types(),
        get_saskatchewan_economic_crop_types(),
        get_manitoba_economic_crop_types(),
        get_ontario_economic_crop_types()))


def get_valid_crop_types() -> list[CropType]:
    return sorted(
        [
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
    )


def get_valid_perennial_types() -> list[CropType]:
    return sorted(
        [
            CropType.ForageForSeed,
            CropType.TameGrass,
            CropType.TameLegume,
            CropType.TameMixed,
            CropType.RangelandNative,
            CropType.SeededGrassland,

        ]
    )


def get_alberta_economic_crop_types() -> list[CropType]:
    return sorted([
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
    ])


def get_saskatchewan_economic_crop_types() -> list[CropType]:
    return [
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


def get_manitoba_economic_crop_types() -> list[CropType]:
    return [
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


def get_ontario_economic_crop_types() -> list[CropType]:
    return [
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


def get_grassland_types() -> list[CropType]:
    return sorted(
        [
            CropType.BrokenGrassland,
            CropType.GrasslandSeeded
        ]
    )


class CropTypeInGui(AutoNameEnum):
    """This class includes all CropType members that are allowed in the GUI of Holos.

    Holos Source Code:
        None. This class was manually written.

    """
    # region Oilseed
    Camelina = CropType.Camelina
    Canola = CropType.Canola
    Flax = CropType.Flax
    Mustard = CropType.Mustard
    Oilseeds = CropType.Oilseeds
    Soybeans = CropType.Soybeans
    # endregion

    # region Other field crops
    BerriesAndGrapes = CropType.BerriesAndGrapes
    OtherFieldCrops = CropType.OtherFieldCrops
    Safflower = CropType.Safflower
    SunflowerSeed = CropType.SunflowerSeed
    Tobacco = CropType.Tobacco
    Vegetables = CropType.Vegetables
    # endregion

    # region Pulse crops
    BeansDryField = CropType.BeansDryField
    Chickpeas = CropType.Chickpeas
    DryFieldPeas = CropType.DryFieldPeas
    Lentils = CropType.Lentils
    PulseCrops = CropType.PulseCrops
    # endregion

    # region Root crops
    Potatoes = CropType.Potatoes
    SugarBeets = CropType.SugarBeets
    # endregion

    # region Silage
    BarleySilage = CropType.BarleySilage
    GrassSilage = CropType.GrassSilage
    OatSilage = CropType.OatSilage
    SilageCorn = CropType.SilageCorn
    TriticaleSilage = CropType.TriticaleSilage
    WheatSilage = CropType.WheatSilage
    # endregion

    # region Small grain cereals
    Barley = CropType.Barley
    Buckwheat = CropType.Buckwheat
    CanarySeed = CropType.CanarySeed
    FallRye = CropType.FallRye
    GrainCorn = CropType.GrainCorn
    MixedGrains = CropType.MixedGrains
    Oats = CropType.Oats
    SmallGrainCereals = CropType.SmallGrainCereals
    Sorghum = CropType.Sorghum
    Triticale = CropType.Triticale
    UndersownBarley = CropType.UndersownBarley
    Wheat = CropType.Wheat
    # endregion

    # region Fallow
    Fallow = CropType.Fallow
    # endregion

    # region Perennial
    ForageForSeed = CropType.ForageForSeed
    RangelandNative = CropType.RangelandNative
    SeededGrassland = CropType.SeededGrassland
    TameGrass = CropType.TameGrass
    TameLegume = CropType.TameLegume
    TameMixed = CropType.TameMixed
    # endregion
