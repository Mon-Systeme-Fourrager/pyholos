from holos_service.common import EnumGeneric


class HousingType(EnumGeneric):
    not_selected: str = "NotSelected"
    confined_no_barn: str = "ConfinedNoBarn"
    """Also known as 'Confined no barn (feedlot)'
    """
    housed_in_barn: str = "HousedInBarn"
    housed_ewes: str = "HousedEwes"
    housed_in_barn_solid: str = "HousedInBarnSolid"
    housed_in_barn_slurry: str = "HousedInBarnSlurry"
    enclosed_pasture: str = "EnclosedPasture"
    open_range_or_hills: str = "OpenRangeOrHills"
    tie_stall: str = "TieStall"
    small_free_stall: str = "SmallFreeStall"
    large_free_stall: str = "LargeFreeStall"
    grazing_under3km: str = "GrazingUnder3km"
    grazing_over3km: str = "GrazingOver3km"
    confined: str = "Confined"
    flat_pasture: str = "FlatPasture"
    hilly_pasture_or_open_range: str = "HillyPastureOrOpenRange"
    pasture: str = "Pasture"
    """Pasture, range, or paddock
    """
    dry_lot: str = "DryLot"
    """Also known as 'Standing or exercise yard'
    """
    swath_grazing: str = "SwathGrazing"
    custom: str = "Custom"
    free_stall_barn_solid_litter: str = "FreeStallBarnSolidLitter"
    free_stall_barn_slurry_scraping: str = "FreeStallBarnSlurryScraping"
    free_stall_barn_flushing: str = "FreeStallBarnFlushing"
    free_stall_barn_milk_parlour_slurry_flushing: str = "FreeStallBarnMilkParlourSlurryFlushing"
    """Also known as 'Milking parlour (slurry - flushing)'
    """
    tie_stall_solid_litter: str = "TieStallSolidLitter"
    """Also known as 'Tie-stall barn (solid)'
    """
    tie_stall_slurry: str = "TieStallSlurry"
    """Also known as 'Tie-stall barn (slurry)'
    """


class HousingTypeExtensions:
    def __init__(
            self,
            housing_type: HousingType
    ):
        # https://github.com/holos-aafc/Holos/blob/53f778f9bd4579d164de10f5b04db34d020b96a9/H.Core/Enumerations/HousingTypeExtensions.cs#L10
        self.is_free_stall = any([housing_type == v for v in (
            housing_type.small_free_stall,
            housing_type.large_free_stall,
            housing_type.free_stall_barn_flushing,
            housing_type.free_stall_barn_milk_parlour_slurry_flushing,
            housing_type.free_stall_barn_slurry_scraping,
            housing_type.free_stall_barn_solid_litter)])

        self.is_tie_stall = any([housing_type == v for v in (
            housing_type.tie_stall,
            housing_type.tie_stall_slurry,
            housing_type.tie_stall_solid_litter)])

        self.is_barn = any([housing_type == v for v in (
            housing_type.housed_in_barn,
            housing_type.housed_in_barn_slurry,
            housing_type.housed_in_barn_solid)])

        self.is_feed_lot = any([housing_type == v for v in (
            housing_type.confined,
            housing_type.confined_no_barn)])

        self.is_electrical_consuming_housing_type = any([
            self.is_free_stall,
            self.is_barn,
            self.is_tie_stall,
            self.is_feed_lot])

        self.is_indoor_housing = any([housing_type == v for v in (
            housing_type.housed_in_barn,
            housing_type.housed_in_barn_slurry,
            housing_type.housed_in_barn_solid,
            housing_type.free_stall_barn_flushing,
            housing_type.free_stall_barn_solid_litter,
            housing_type.free_stall_barn_slurry_scraping,
            housing_type.free_stall_barn_milk_parlour_slurry_flushing)])

        self.is_pasture = any([housing_type == v for v in (
            housing_type.pasture,
            housing_type.enclosed_pasture,
            housing_type.flat_pasture,
            housing_type.grazing_over3km,
            housing_type.grazing_under3km,
            housing_type.hilly_pasture_or_open_range,
            housing_type.open_range_or_hills,
            housing_type.swath_grazing)])
