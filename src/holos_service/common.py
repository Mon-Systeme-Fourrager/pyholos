from enum import Enum
from typing import Any

from holos_service import django_stuff


class EnumGeneric(Enum):
    @classmethod
    def get_value(cls, name: str) -> str:
        return getattr(cls, name).value

    @classmethod
    def get_member(cls, name: str):
        return getattr(cls, name)


class HolosVar:
    def __init__(
            self,
            name: str,
            value: Any
    ):
        self.name = name
        self.value = value


class Component:
    def __init__(self):
        pass

    def to_dict(self) -> dict:
        return {v.name: v.value for k, v in self.__dict__.items() if isinstance(v, HolosVar)}


class Region:
    EasternCanada: str = "EasternCanada"
    WesternCanada: str = "WesternCanada"


def get_region(
        province: str
) -> str:
    if any([
        province == django_stuff.CanadianProvince.Alberta.name,
        province == django_stuff.CanadianProvince.BritishColumbia.name,
        province == django_stuff.CanadianProvince.Manitoba.name,
        province == django_stuff.CanadianProvince.Saskatchewan.name,
        province == django_stuff.CanadianProvince.NorthwestTerritories.name,
        province == django_stuff.CanadianProvince.Nunavut.name]):

        res = Region.WesternCanada

    else:
        res = Region.EasternCanada

    return res
