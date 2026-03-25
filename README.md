# MitoGeneMap.py
Python script for mapping gene identifiers (Entrez ID) and integrating MAGMA gene-based results with the Human MitoCarta 3.0 database.

## Usage

### 1. Requirements
- Python 3.x
- pandas

Install dependencies:
pip install pandas openpyxl

### 2. Input files

- MAGMA output file (.genes.out)
- MitoCarta 3.0 file (.xlsx)

### 3. Configure paths

Edit the file paths inside the script:

magma_file = "path/to/MAGMA.genes.out"
mitocarta_file = "path/to/Human.MitoCarta3.0.xlsx"
mitocarta_sheet = "A Human MitoCarta3.0"

### 4. Run the script

python MitoGeneMap.py

### 5. Output files

The script generates:

- MAGMA_genes_in_MitoCarta_with_SYMBOL.tsv  
  -> Genes successfully mapped to MitoCarta

- MAGMA_genes_not_in_MitoCarta.tsv  
  -> Genes without match

- MAGMA_MitoCarta_statistics.txt  
  -> Summary statistics of the mapping process

### 6. Notes

- Gene identifiers must match Entrez Gene IDs
- Genes without valid mapping are automatically excluded
