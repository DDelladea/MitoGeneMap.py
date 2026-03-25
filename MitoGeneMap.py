import pandas as pd

    #Loads df_MAGMA data 
def load_magma(filepath: str) -> pd.DataFrame:
    df = pd.read_csv(filepath, sep=r"\s+")
    df["GENE"] = df["GENE"].astype(str)
    return df

    #Load data df_Mitocarta
def load_mitocarta(filepath: str, sheet: str) -> pd.DataFrame:
    df = pd.read_excel(filepath, sheet_name=sheet)
    df["HumanGeneID"] = df["HumanGeneID"].astype(str)
    return df[["HumanGeneID", "Symbol"]]

    #Merge data
def merge_datasets(magma_df: pd.DataFrame, mc_df: pd.DataFrame) -> pd.DataFrame:
    merged = magma_df.merge(
        mc_df,
        left_on="GENE",
        right_on="HumanGeneID",
        how="left"
    )
    merged = merged.rename(columns={"Symbol": "GENE_SYMBOL"})
    return merged.drop(columns=["HumanGeneID"])


def split_presence(df: pd.DataFrame):
    present = df[df["GENE_SYMBOL"].notna()]
    absent = df[df["GENE_SYMBOL"].isna()]
    return present, absent


def compute_statistics(magma_df: pd.DataFrame, present_df: pd.DataFrame, absent_df: pd.DataFrame):
    total = magma_df["GENE"].nunique()
    found = present_df["GENE"].nunique()
    not_found = absent_df["GENE"].nunique()

    return {
        "total": total,
        "found": found,
        "not_found": not_found,
        "pct_found": (found / total) * 100,
        "pct_not_found": (not_found / total) * 100
    }

    #Function saves the results as a .csv file.
def save_outputs(present_df: pd.DataFrame, absent_df: pd.DataFrame):
    present_df.to_csv("MAGMA_genes_in_MitoCarta_with_SYMBOL.tsv", sep="\t", index=False)
    absent_df.to_csv("MAGMA_genes_not_in_MitoCarta.tsv", sep="\t", index=False)

    #Function create and save statistics file
def save_statistics(stats: dict):
    with open("MAGMA_MitoCarta_statistics.txt", "w") as f:
        f.write("Comparison statistics ===\n\n")
        f.write(f"Total genes in MAGMA: {stats['total']}\n")
        f.write(f"Genes found in MitoCarta: {stats['found']} ({stats['pct_found']:.2f}%)\n")
        f.write(f"Genes not found: {stats['not_found']} ({stats['pct_not_found']:.2f}%)\n")
        f.write("\nGenerated files:\n")
        f.write(" - MAGMA_genes_in_MitoCarta_with_SYMBOL.tsv\n")
        f.write(" - MAGMA_genes_not_in_MitoCarta.tsv\n")


def main():
    #Enter the data to be analyzed:
    magma_file = r"D:\Doutorado\Mitogenomas\GWAS\ResultsAnalysisV37\MAGMA_V37_GBA_VelocidadeMarcha.genes.out"
    mitocarta_file = r"D:\Doutorado\Mitogenomas\GWAS\ResultsAnalysisV37\Human.MitoCarta3.0.xls"
    mitocarta_sheet = "A Human MitoCarta3.0"

    magma_df = load_magma(magma_file)
    mc_df = load_mitocarta(mitocarta_file, mitocarta_sheet)

    merged_df = merge_datasets(magma_df, mc_df)
    present_df, absent_df = split_presence(merged_df)

    stats = compute_statistics(magma_df, present_df, absent_df)

    save_outputs(present_df, absent_df)
    save_statistics(stats)

    print("Completed.")
    print("Statistics file created: MAGMA_MitoCarta_statistics.txt")


if __name__ == "__main__":
    main()
