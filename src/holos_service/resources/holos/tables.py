from pathlib import Path

from pandas import DataFrame

from holos_service.components.animals.common import AnimalType, BeddingMaterialType
from holos_service.config import PathsHolosResources


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
            'source: https://github.com/holos-aafc/Holos/blob/396f1ab9bc7247e6d78766f9445c14d2eb7c0d9d'
            '/H.Core/Providers/Animals/Table_30_Default_Bedding_Material_Composition_Provider.cs#L15'
        ])
    pass


if __name__ == '__main__':
    set_table_30()
