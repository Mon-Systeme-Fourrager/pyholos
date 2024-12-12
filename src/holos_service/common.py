from enum import Enum


class EnumGeneric(Enum):
    @classmethod
    def get_value(cls, name: str) -> str:
        return getattr(cls, name).value

    @classmethod
    def get_member(cls, name: str):
        return getattr(cls, name)
