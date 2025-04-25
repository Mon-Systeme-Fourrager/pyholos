"""This module includes figures produced for performing a demo on MSF
"""
from dataclasses import dataclass
from pathlib import Path

import matplotlib
from matplotlib import pyplot
from pandas import DataFrame

matplotlib.use("Qt5Agg")


class UnitStrings:
    co2_eq = r"$\mathregular{CO_2\/(eq)}$"
    mg_co2_eq = f'MG {co2_eq}'
    ch4 = r"$\mathregular{CH_4}$"
    n2o = r"$\mathregular{N_2O}$"
    co2 = r"$\mathregular{CO_2}$"


@dataclass
class NameUnit:
    name: str
    unit: str

    def get_string(self, sep: str = ' ') -> str:
        return sep.join([self.name, self.unit])


class Config:
    map_names: dict[str, NameUnit] = {
        "Enteric CH4 (Mg C02e)": NameUnit(name=f"Enteric {UnitStrings.ch4}", unit=UnitStrings.mg_co2_eq),
        "Manure CH4 (Mg C02e)": NameUnit(name=f"Manure {UnitStrings.ch4}", unit=UnitStrings.mg_co2_eq),
        "Direct N2O (Mg C02e)": NameUnit(name=f"Direct {UnitStrings.n2o}", unit=UnitStrings.mg_co2_eq),
        "Indirect N2O (Mg C02e)": NameUnit(name=f"Indirect {UnitStrings.n2o}", unit=UnitStrings.mg_co2_eq),
        "Energy CO2 (Mg C02e)": NameUnit(name=f"Energy {UnitStrings.co2}", unit=UnitStrings.mg_co2_eq),
        "CO2 (Mg C02e)": NameUnit(name=f"{UnitStrings.co2}", unit=UnitStrings.mg_co2_eq),
        "Sub-total (Mg C02e)": NameUnit(name=f"Sub-total {UnitStrings.co2}", unit=UnitStrings.mg_co2_eq),
    }


def plot_farm_total_co2eq_emissions(
        df: DataFrame,
        path_dir_fig: Path
) -> None:
    data = df.drop(columns=['Farm Name', 'Component Name', 'Component Group Name', 'Sub-total (Mg C02e)']).groupby(
        'Component Category').sum()

    fig, ax = pyplot.subplots()
    data.plot(kind='bar', stacked=True, ax=ax)
    ax.set(
        xlabel="Animal category",
        ylabel=UnitStrings.co2_eq
    )
    ax.tick_params(axis='x', labelrotation=45)

    handles, labels = ax.get_legend_handles_labels()
    ax.legend(
        labels=[Config.map_names[s].name for s in labels],
        handles=handles
    )

    fig.tight_layout()
    fig.savefig(path_dir_fig / f"co2eq_{df['Farm Name'].iloc[0]}_total.png")
    pass


def plot_farm_detailed_co2eq_emissions(
        df: DataFrame,
        path_dir_fig: Path
) -> None:
    data = df.drop(columns=['Farm Name', 'Component Name', 'Sub-total (Mg C02e)']).groupby(
        by=['Component Category', 'Component Group Name']).sum()

    fig, ax = pyplot.subplots()
    data.plot(kind='bar', stacked=True, ax=ax)
    ax.set(
        xlabel="Animal category",
        ylabel=UnitStrings.co2_eq
    )

    handles, labels = ax.get_legend_handles_labels()
    ax.legend(
        labels=[Config.map_names[s].name for s in labels],
        handles=handles
    )

    fig.tight_layout()
    fig.savefig(path_dir_fig / f"co2eq_{df['Farm Name'].iloc[0]}_detailed.png")
    pass


def plot_total_co2eq_emissions(
        ghg_data: DataFrame,
        path_dir_fig: Path,
        farm_name: str | list[str] = None
) -> None:
    if farm_name is not None:
        farms = farm_name if isinstance(farm_name, list) else [farm_name]
    else:
        farms = ghg_data['Farm Name'].unique()

    for farm in farms:
        plot_farm_total_co2eq_emissions(
            df=ghg_data[ghg_data['Farm Name'] == farm],
            path_dir_fig=path_dir_fig
        )
        plot_farm_detailed_co2eq_emissions(
            df=ghg_data[ghg_data['Farm Name'] == farm],
            path_dir_fig=path_dir_fig
        )

    pass
