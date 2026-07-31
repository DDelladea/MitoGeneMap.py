import pandas as pd
import os


# Input files

FILES = {

    "MAGMA": r"Path/To/MAGMA_File.genes.out",

    "MitoCarta": r"Path/To/Human.MitoCarta3.0.xls"

}


MITOCARTA_SHEET = "A Human MitoCarta3.0"


# Output directory

OUTPUT_DIR = r"Path/To/Output/"


os.makedirs(
    OUTPUT_DIR,
    exist_ok=True
)



def load_magma(filepath):

    df = pd.read_csv(
        filepath,
        sep=r"\s+"
    )

    df["GENE"] = (
        df["GENE"]
        .astype(str)
    )

    return df



def load_mitocarta(filepath, sheet):

    df = pd.read_excel(
        filepath,
        sheet_name=sheet
    )


    df["HumanGeneID"] = (

        df["HumanGeneID"]
        .astype(str)

    )


    return df[

        [
            "HumanGeneID",
            "Symbol"
        ]

    ]



def map_genes(magma_df, mitocarta_df):

    mapped = magma_df.merge(

        mitocarta_df,

        left_on="GENE",

        right_on="HumanGeneID",

        how="left"

    )


    mapped = mapped.rename(

        columns={
            "Symbol": "GENE_SYMBOL"
        }

    )


    mapped = mapped.drop(

        columns=[
            "HumanGeneID"
        ]

    )


    return mapped



def split_results(mapped_df):

    mapped = mapped_df[
        mapped_df["GENE_SYMBOL"].notna()
    ]


    not_mapped = mapped_df[
        mapped_df["GENE_SYMBOL"].isna()
    ]


    return mapped, not_mapped



def calculate_statistics(magma_df, mapped_df, not_mapped_df):


    total = magma_df["GENE"].nunique()

    mapped = mapped_df["GENE"].nunique()

    not_mapped = not_mapped_df["GENE"].nunique()


    return {

        "total": total,

        "mapped": mapped,

        "not_mapped": not_mapped,

        "mapped_percentage":
            (mapped / total) * 100,

        "not_mapped_percentage":
            (not_mapped / total) * 100

    }



def save_results(mapped_df, not_mapped_df):


    mapped_df.to_csv(

        OUTPUT_DIR +
        "MAGMA_genes_in_MitoCarta_with_SYMBOL.tsv",

        sep="\t",

        index=False

    )


    not_mapped_df.to_csv(

        OUTPUT_DIR +
        "MAGMA_genes_not_in_MitoCarta.tsv",

        sep="\t",

        index=False

    )



def save_report(stats):


    with open(

        OUTPUT_DIR +
        "MAGMA_MitoCarta_statistics.txt",

        "w",

        encoding="utf-8"

    ) as file:


        file.write(
            "MAGMA and MitoCarta mapping summary\n\n"
        )


        file.write(
            f"Total MAGMA genes: {stats['total']}\n"
        )


        file.write(

            f"Genes mapped to MitoCarta: "
            f"{stats['mapped']} "
            f"({stats['mapped_percentage']:.2f}%)\n"

        )


        file.write(

            f"Genes not mapped: "
            f"{stats['not_mapped']} "
            f"({stats['not_mapped_percentage']:.2f}%)\n"

        )


        file.write(
            "\nGenerated files:\n"
        )


        file.write(
            "- MAGMA_genes_in_MitoCarta_with_SYMBOL.tsv\n"
        )


        file.write(
            "- MAGMA_genes_not_in_MitoCarta.tsv\n"
        )



def main():


    magma = load_magma(

        FILES["MAGMA"]

    )


    mitocarta = load_mitocarta(

        FILES["MitoCarta"],

        MITOCARTA_SHEET

    )


    mapped = map_genes(

        magma,

        mitocarta

    )


    mapped_df, not_mapped_df = split_results(

        mapped

    )


    stats = calculate_statistics(

        magma,

        mapped_df,

        not_mapped_df

    )


    save_results(

        mapped_df,

        not_mapped_df

    )


    save_report(

        stats

    )


    print(
        "MitoCarta mapping completed."
    )



if __name__ == "__main__":

    main()