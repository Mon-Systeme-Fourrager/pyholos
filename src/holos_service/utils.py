import re
from enum import StrEnum
from pathlib import Path

from pandas import read_csv, DataFrame

from holos_service.core_constants import CoreConstants


class AutoName(StrEnum):
    """Allows automatically setting the member value identical to the member name."""

    def _generate_next_value_(self, start, count, last_values):
        return self


def read_holos_resource_table(
        path_file: Path,
        **kwargs
) -> DataFrame:
    return read_csv(path_file, sep=',', decimal='.', comment='#', **kwargs
                    ).replace({
        'NotApplicable': CoreConstants.NotApplicable,
        float('nan'): None})


def get_local_args(kwargs: dict) -> dict:
    return {k: v for k, v in kwargs.items() if not any([k.startswith('_'), k == 'self'])}


def convert_camel_case_to_space_delimited(s: str) -> str:
    return re.sub("([a-z])([A-Z])", "\g<1> \g<2>", s)


def concat_lists(*args) -> list:
    return [v for l in args for v in l]
