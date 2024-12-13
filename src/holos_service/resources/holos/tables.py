from pathlib import Path

from pandas import DataFrame

from holos_service.components.animals.common import AnimalType, BeddingMaterialType
from holos_service.config import PathsHolosResources
from holos_service.core_constants import CoreConstants


class HolosTable:
    def __init__(
            self,
            name: str,
            data: list | DataFrame,
            path: Path
    ):
        self.name = name
        self.data = data
        self.path = path

    def write_data_to_csv(
            self,
            comments: list[str] | str = None
    ) -> None:
        if comments is None:
            comments = []
        elif isinstance(comments, str):
            comments = [comments]

        comments.insert(0, f'This table was automatically generated using "{Path(__file__).name}"')

        with self.path.open(mode='w', newline='') as f:
            for comment in comments:
                f.write(f'# {comment}\n')
            f.write('#\n')

            DataFrame.from_records(self.data).to_csv(f, sep=',', decimal='.', index=False)


def set_table_16():
    table_16 = HolosTable(
        name='Table_16_Livestock_Coefficients_BeefAndDairy_Cattle_Provider',
        data=[
            # Beef Cattle Data Sources :

            # BaselineMaintenanceCoefficient = IPCC (2019, Table 10.4)
            # GainCoefficient = IPCC (2019, Eq. 10.6)
            # DefaultInitialWeight = Sheppard et al. (2015) , A.Alemu(pers.comm, 2022)
            # DefaultFinalWeight = Sheppard et al. (2015) , A.Alemu(pers.comm, 2022)

            dict(
                AnimalType=AnimalType.beef_calf.value,
                BaselineMaintenanceCoefficient=CoreConstants.NotApplicable,
                GainCoefficient=CoreConstants.NotApplicable,
                DefaultInitialWeight=39,
                DefaultFinalWeight=260
            ),
            dict(
                AnimalType=AnimalType.beef_cow_lactating.value,
                BaselineMaintenanceCoefficient=0.386,
                GainCoefficient=0.8,
                DefaultInitialWeight=610,
                DefaultFinalWeight=610
            ),
            dict(
                AnimalType=AnimalType.beef_cow_dry.value,
                BaselineMaintenanceCoefficient=0.322,
                GainCoefficient=0.8,
                DefaultInitialWeight=610,
                DefaultFinalWeight=610
            ),
            dict(
                AnimalType=AnimalType.beef_bulls.value,
                BaselineMaintenanceCoefficient=0.370,
                GainCoefficient=1.2,
                DefaultInitialWeight=900,
                DefaultFinalWeight=900
            ),
            dict(
                AnimalType=AnimalType.beef_backgrounder_steer.value,
                BaselineMaintenanceCoefficient=0.322,
                GainCoefficient=1,
                DefaultInitialWeight=250,
                DefaultFinalWeight=380
            ),
            # Aklilu says these two animal groups have the same values
            dict(
                AnimalType=AnimalType.beef_backgrounder_heifer.value,
                BaselineMaintenanceCoefficient=0.322,
                GainCoefficient=0.8,
                DefaultInitialWeight=240,
                DefaultFinalWeight=360
            ),
            dict(
                AnimalType=AnimalType.beef_replacement_heifers.value,
                BaselineMaintenanceCoefficient=0.322,
                GainCoefficient=0.8,
                DefaultInitialWeight=240,
                DefaultFinalWeight=360
            ),
            dict(
                AnimalType=AnimalType.beef_finishing_steer.value,
                BaselineMaintenanceCoefficient=0.322,
                GainCoefficient=1.0,
                DefaultInitialWeight=310,
                DefaultFinalWeight=610
            ),
            dict(
                AnimalType=AnimalType.beef_finishing_heifer.value,
                BaselineMaintenanceCoefficient=0.322,
                GainCoefficient=0.8,
                DefaultInitialWeight=300,
                DefaultFinalWeight=580
            ),

            # """
            # Dairy Cattle
            # Footnote 1
            # Dairy Cattle Data Sources :
            # BaselineMaintenanceCoefficient = IPCC (2019, Table 10.4)
            # GainCoefficient = IPCC (2019, Eq. 10.6)
            # DefaultInitialWeight = Lactanet (2020)
            # DefaultFinalWeight = Lactanet (2020)
            # """

            dict(
                AnimalType=AnimalType.dairy_lactating_cow.value,
                BaselineMaintenanceCoefficient=0.386,
                GainCoefficient=0.8,
                DefaultInitialWeight=687,
                DefaultFinalWeight=687
            ),
            dict(
                AnimalType=AnimalType.dairy_dry_cow.value,
                BaselineMaintenanceCoefficient=0.322,
                GainCoefficient=0.8,
                DefaultInitialWeight=687,
                DefaultFinalWeight=687
            ),
            dict(
                AnimalType=AnimalType.dairy_heifers.value,
                BaselineMaintenanceCoefficient=0.322,
                GainCoefficient=0.8,
                DefaultInitialWeight=637,
                DefaultFinalWeight=687
            ),
            dict(
                AnimalType=AnimalType.dairy_bulls.value,
                BaselineMaintenanceCoefficient=0.37,
                GainCoefficient=1.2,
                DefaultInitialWeight=1200,
                DefaultFinalWeight=1200
            ),
            dict(
                AnimalType=AnimalType.dairy_calves.value,
                BaselineMaintenanceCoefficient=0,
                GainCoefficient=0,
                DefaultInitialWeight=45,
                DefaultFinalWeight=127
            )
        ],
        path=PathsHolosResources.Table_16_Livestock_Coefficients_BeefAndDairy_Cattle_Provider
    )

    table_16.write_data_to_csv(
        comments=[
            'Table 16. Livestock coefficients for beef cattle and dairy cattle.',
            'source: https://github.com/holos-aafc/Holos/blob/396f1ab9bc7247e6d78766f9445c14d2eb7c0d9d/H.Core/Providers/Animals/Table_16_Livestock_Coefficients_BeefAndDairy_Cattle_Provider.cs#L13'
        ])


def set_table_30():
    table_30 = HolosTable(
        name='Table_30_Default_Bedding_Material_Composition_Provider',
        data=[
            # Beef
            dict(
                AnimalType=AnimalType.beef.value,
                BeddingMaterial=BeddingMaterialType.straw.value,  # Footnote 1
                TotalNitrogenKilogramsDryMatter=0.0057,
                TotalCarbonKilogramsDryMatter=0.447,
                TotalPhosphorusKilogramsDryMatter=0.000635,
                CarbonToNitrogenRatio=90.5,
                MoistureContent=9.57  # Footnote 12
            ),
            dict(
                AnimalType=AnimalType.beef.value,
                BeddingMaterial=BeddingMaterialType.wood_chip.value,  # Footnotes 1, 2
                TotalNitrogenKilogramsDryMatter=0.00185,
                TotalCarbonKilogramsDryMatter=0.506,
                TotalPhosphorusKilogramsDryMatter=0.000275,
                CarbonToNitrogenRatio=329.5,
                MoistureContent=12.82  # Footnote12
            ),
            # Dairy
            dict(
                AnimalType=AnimalType.dairy.value,
                BeddingMaterial=BeddingMaterialType.sand.value  # Footnote 4
            ),
            dict(
                AnimalType=AnimalType.dairy.value,
                BeddingMaterial=BeddingMaterialType.separated_manure_solid.value,  # Footnote 5
                TotalNitrogenKilogramsDryMatter=0.033,
                TotalCarbonKilogramsDryMatter=0.395,
                TotalPhosphorusKilogramsDryMatter=0,
                CarbonToNitrogenRatio=12,
                MoistureContent=0
            ),
            dict(
                AnimalType=AnimalType.dairy.value,
                BeddingMaterial=BeddingMaterialType.straw_long.value,  # Footnote 6
                TotalNitrogenKilogramsDryMatter=0.0057,
                TotalCarbonKilogramsDryMatter=0.447,
                TotalPhosphorusKilogramsDryMatter=0.000635,
                CarbonToNitrogenRatio=90.5,
                MoistureContent=9.57  # Footnote 12
            ),
            dict(
                AnimalType=AnimalType.dairy.value,
                BeddingMaterial=BeddingMaterialType.straw_chopped.value,  # Footnote 6
                TotalNitrogenKilogramsDryMatter=0.0057,
                TotalCarbonKilogramsDryMatter=0.447,
                TotalPhosphorusKilogramsDryMatter=0.000635,
                CarbonToNitrogenRatio=90.5,
                MoistureContent=9.57  # Footnote 12
            ),
            dict(
                AnimalType=AnimalType.dairy.value,
                BeddingMaterial=BeddingMaterialType.shavings.value,  # Footnotes 4, 7
                TotalNitrogenKilogramsDryMatter=0.00185,
                TotalCarbonKilogramsDryMatter=0.506,
                TotalPhosphorusKilogramsDryMatter=0.000275,
                CarbonToNitrogenRatio=329.5,
                MoistureContent=10.09  # Footnote 12
            ),
            dict(
                AnimalType=AnimalType.dairy.value,
                BeddingMaterial=BeddingMaterialType.sawdust.value,  # Footnotes 4, 7
                TotalNitrogenKilogramsDryMatter=0.00185,
                TotalCarbonKilogramsDryMatter=0.506,
                TotalPhosphorusKilogramsDryMatter=0.000275,
                CarbonToNitrogenRatio=329.5,
                MoistureContent=10.99  # Footnote 12
            ),
            # Swine
            dict(
                AnimalType=AnimalType.swine.value,
                BeddingMaterial=BeddingMaterialType.straw_long.value,  # Footnotes 4, 9
                TotalNitrogenKilogramsDryMatter=0.0057,
                TotalCarbonKilogramsDryMatter=0.447,
                TotalPhosphorusKilogramsDryMatter=0.000635,
                CarbonToNitrogenRatio=90.5,
                MoistureContent=9.57  # Footnote 12
            ),
            dict(
                AnimalType=AnimalType.swine.value,
                BeddingMaterial=BeddingMaterialType.straw_chopped.value,  # Footnotes 4, 9
                TotalNitrogenKilogramsDryMatter=0.0057,
                TotalCarbonKilogramsDryMatter=0.447,
                TotalPhosphorusKilogramsDryMatter=0.000635,
                CarbonToNitrogenRatio=90.5,
                MoistureContent=9.57  # Footnote 12
            ),
            # Sheep
            dict(
                AnimalType=AnimalType.sheep.value,
                BeddingMaterial=BeddingMaterialType.straw.value,  # Footnote 7
                TotalNitrogenKilogramsDryMatter=0.0057,
                TotalCarbonKilogramsDryMatter=0.447,
                TotalPhosphorusKilogramsDryMatter=0.000635,
                CarbonToNitrogenRatio=90.5,
                MoistureContent=9.57  # Footnote 12
            ),
            dict(
                AnimalType=AnimalType.sheep.value,
                BeddingMaterial=BeddingMaterialType.shavings.value,  # Footnote 7
                TotalNitrogenKilogramsDryMatter=0.00185,
                TotalCarbonKilogramsDryMatter=0.506,
                TotalPhosphorusKilogramsDryMatter=0.000275,
                CarbonToNitrogenRatio=329.5,
                MoistureContent=10.09  # Footnote 12
            ),
            # Poultry
            dict(
                AnimalType=AnimalType.poultry.value,
                BeddingMaterial=BeddingMaterialType.straw.value,  # Footnote 9
                TotalNitrogenKilogramsDryMatter=0.0057,
                TotalCarbonKilogramsDryMatter=0.447,
                TotalPhosphorusKilogramsDryMatter=0.000635,
                CarbonToNitrogenRatio=90.5,
                MoistureContent=9.57  # Footnote 12
            ),
            dict(
                AnimalType=AnimalType.poultry.value,
                BeddingMaterial=BeddingMaterialType.shavings.value,  # Footnote 9
                TotalNitrogenKilogramsDryMatter=0.00185,
                TotalCarbonKilogramsDryMatter=0.506,
                TotalPhosphorusKilogramsDryMatter=0.000275,
                CarbonToNitrogenRatio=329.5,
                MoistureContent=10.09  # Footnote 12
            ),
            dict(
                AnimalType=AnimalType.poultry.value,
                BeddingMaterial=BeddingMaterialType.sawdust.value,  # Footnotes 4, 7
                TotalNitrogenKilogramsDryMatter=0.00185,
                TotalCarbonKilogramsDryMatter=0.506,
                TotalPhosphorusKilogramsDryMatter=0.000275,
                CarbonToNitrogenRatio=329.5,
                MoistureContent=10.99  # Footnote 12
            ),
            # Other Livestock
            dict(
                AnimalType=AnimalType.llamas.value,
                BeddingMaterial=BeddingMaterialType.straw.value,
                MoistureContent=9.57,
                TotalNitrogenKilogramsDryMatter=0.0057,
                TotalCarbonKilogramsDryMatter=0.447,
                TotalPhosphorusKilogramsDryMatter=0.000635,
                CarbonToNitrogenRatio=90.5  # Footnote 12
            ),
            dict(
                AnimalType=AnimalType.alpacas.value,
                BeddingMaterial=BeddingMaterialType.straw.value,
                MoistureContent=9.57,
                TotalNitrogenKilogramsDryMatter=0.0057,
                TotalCarbonKilogramsDryMatter=0.447,
                TotalPhosphorusKilogramsDryMatter=0.000635,
                CarbonToNitrogenRatio=90.5  # Footnote 12
            ),
            dict(
                AnimalType=AnimalType.deer.value,
                BeddingMaterial=BeddingMaterialType.straw.value,
                MoistureContent=9.57,
                TotalNitrogenKilogramsDryMatter=0.0057,
                TotalCarbonKilogramsDryMatter=0.447,
                TotalPhosphorusKilogramsDryMatter=0.000635,
                CarbonToNitrogenRatio=90.5  # Footnote 12
            ),
            dict(
                AnimalType=AnimalType.elk.value,
                BeddingMaterial=BeddingMaterialType.straw.value,
                MoistureContent=9.57,
                TotalNitrogenKilogramsDryMatter=0.0057,
                TotalCarbonKilogramsDryMatter=0.447,
                TotalPhosphorusKilogramsDryMatter=0.000635,
                CarbonToNitrogenRatio=90.5  # Footnote 12
            ),
            dict(
                AnimalType=AnimalType.goats.value,
                BeddingMaterial=BeddingMaterialType.straw.value,
                MoistureContent=9.57,
                TotalNitrogenKilogramsDryMatter=0.0057,
                TotalCarbonKilogramsDryMatter=0.447,
                TotalPhosphorusKilogramsDryMatter=0.000635,
                CarbonToNitrogenRatio=90.5  # Footnote 12
            ),
            dict(
                AnimalType=AnimalType.horses.value,
                BeddingMaterial=BeddingMaterialType.straw.value,
                MoistureContent=9.57,
                TotalNitrogenKilogramsDryMatter=0.0057,
                TotalCarbonKilogramsDryMatter=0.447,
                TotalPhosphorusKilogramsDryMatter=0.000635,
                CarbonToNitrogenRatio=90.5  # Footnote 12
            ),
            dict(
                AnimalType=AnimalType.mules.value,
                BeddingMaterial=BeddingMaterialType.straw.value,
                MoistureContent=9.57,
                TotalNitrogenKilogramsDryMatter=0.0057,
                TotalCarbonKilogramsDryMatter=0.447,
                TotalPhosphorusKilogramsDryMatter=0.000635,
                CarbonToNitrogenRatio=90.5  # Footnote 12
            ),
            dict(
                AnimalType=AnimalType.bison.value,
                BeddingMaterial=BeddingMaterialType.straw.value,
                MoistureContent=9.57,
                TotalNitrogenKilogramsDryMatter=0.0057,
                TotalCarbonKilogramsDryMatter=0.447,
                TotalPhosphorusKilogramsDryMatter=0.000635,
                CarbonToNitrogenRatio=90.5  # Footnote 12
            )
        ],
        path=PathsHolosResources.Table_30_Default_Bedding_Material_Composition_Provider)
    table_30.write_data_to_csv(
        comments=[
            'Table 30. Default bedding application rates and composition of bedding materials for all livestock groups.',
            'source: https://github.com/holos-aafc/Holos/blob/396f1ab9bc7247e6d78766f9445c14d2eb7c0d9d/H.Core/Providers/Animals/Table_30_Default_Bedding_Material_Composition_Provider.cs#L15'
        ])
    pass


if __name__ == '__main__':
    set_table_16()
    set_table_30()
