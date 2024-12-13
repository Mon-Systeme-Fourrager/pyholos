from pathlib import Path

from pandas import read_csv, DataFrame

from holos_service.core_constants import CoreConstants


def read_holos_resource_table(
        path_file: Path,
        **kwargs
) -> DataFrame:
    return read_csv(path_file, sep=',', decimal='.', comment='#', **kwargs
                    ).replace({
        'NotApplicable': CoreConstants.NotApplicable,
        float('nan'): None})
