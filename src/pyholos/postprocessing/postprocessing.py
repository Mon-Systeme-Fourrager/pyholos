from pathlib import Path

from pandas import read_csv, DataFrame


def get_ghg_emissions(
        path_outputs: Path
) -> DataFrame:
    df = read_csv(path_outputs, decimal='.', sep=',').rename(columns=lambda x: x.strip()).ffill()
    cols_to_keep = [s for s in df.columns if "Unnamed" not in s]
    df = df[cols_to_keep].dropna(axis=0)
    df.loc[:, 'Farm Name'] = df['Farm Name'].apply(lambda x: x.replace('_Farm_', '')).to_list()

    df = df[~df['Component Group Name'].str.contains('Totals')]
    df = df[~df['Farm Name'].str.contains('All Farms')]

    return df
