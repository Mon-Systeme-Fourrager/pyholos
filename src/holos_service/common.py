from enum import Enum
from typing import Any


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
        return {k: v.value for k, v in self.__dict__.items() if isinstance(v, HolosVar)}
