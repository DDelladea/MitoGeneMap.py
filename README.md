# MitoGeneMap

Python-based scripts for identification of mitochondrial genes from genomic and transcriptomic association analyses using the MitoCarta3.0 database.

## Overview

MitoGeneMap is a collection of Python scripts developed to identify mitochondrial genes among significant results obtained from large-scale association analyses.

The scripts perform the integration between phenotype-associated genes and mitochondrial annotations available in the MitoCarta3.0 database.

This tool was developed to support mitochondrial gene prioritization analyses by mapping significant genes obtained from:

* Gene-Based Analysis (GBA);
* Transcriptome-Wide Association Study using Joint-Tissue Imputation (TWAS-JTI).

The output consists of mitochondrial gene sets that can be subsequently used for downstream analyses, including overlap and consensus identification.

---

# Workflow overview

The general workflow consists of comparing significant genes obtained from association analyses against mitochondrial gene annotations.

```text
MAGMA Gene-Based Analysis
          |
          ↓
   MitoGeneMap_GBA.py
          |
          ↓
Mitochondrial genes identified


TWAS-JTI analysis
          |
          ↓
  MitoGeneMap_TWAS.py
          |
          ↓
Mitochondrial genes identified
```

---

# Scripts description

## MitoGeneMap_GBA.py

### Purpose

Identifies mitochondrial genes among significant genes obtained from MAGMA Gene-Based Analysis by comparison with the MitoCarta3.0 database.

### Input files

#### MAGMA output

Required column:

```text
GENE
```

The script was designed for MAGMA Gene-Based Analysis output files.

#### MitoCarta3.0 database

Required file:

```text
Human.MitoCarta3.0.xls
```

Required sheet:

```text
A Human MitoCarta3.0
```

---

### Processing

The script:

1. Loads MAGMA gene-based results;
2. Loads mitochondrial gene annotations from MitoCarta3.0;
3. Compares MAGMA genes against MitoCarta3.0;
4. Separates genes identified in MitoCarta3.0 from genes not present in the database;
5. Generates mapping statistics.

---

### Output files

The script generates:

```text
MAGMA_genes_in_MitoCarta_with_SYMBOL.tsv
```

Genes identified as mitochondrial according to MitoCarta3.0.

```text
MAGMA_genes_not_in_MitoCarta.tsv
```

Genes not identified in the mitochondrial database.

```text
MAGMA_MitoCarta_statistics.txt
```

Summary statistics describing the mapping process.

---

# MitoGeneMap_TWAS.py

## Purpose

Identifies mitochondrial genes among significant TWAS-JTI results by comparison with MitoCarta3.0.

---

## Input files

### TWAS-JTI output

Required column:

```text
genename
```

The script was designed for TWAS-JTI output files containing gene symbols.

### MitoCarta3.0 database

Required file:

```text
Human.MitoCarta3.0.xls
```

Required sheet:

```text
A Human MitoCarta3.0
```

---

## Processing

The script:

1. Loads TWAS-JTI significant genes;
2. Loads mitochondrial gene annotations from MitoCarta3.0;
3. Compares TWAS genes against mitochondrial gene symbols;
4. Separates mitochondrial and non-mitochondrial genes;
5. Generates mapping statistics.

---

## Output files

The script generates:

```text
TWAS_genes_in_MitoCarta.txt
```

Genes identified as mitochondrial according to MitoCarta3.0.

```text
TWAS_genes_NOT_in_MitoCarta.txt
```

Genes not identified in the mitochondrial database.

```text
TWAS_MitoCarta_statistics.txt
```

Summary statistics describing the mapping process.

---

# Requirements

Python version:

```text
Python ≥ 3.8
```

Required packages:

```text
pandas
openpyxl
```

Install dependencies:

```bash
pip install pandas openpyxl
```

---

# Usage

1. Clone this repository.

2. Install dependencies.

3. Open the desired script.

4. Update the input and output paths:

Example:

```python
FILES = {

    "Input": "Path/To/File"

}
```

5. Run the script:

```bash
python MitoGeneMap_GBA.py
```

or

```bash
python MitoGeneMap_TWAS.py
```

---

# Data source

Mitochondrial annotations are obtained from:

MitoCarta3.0 database.

The scripts are designed to work with mitochondrial gene identification workflows from:

* MAGMA Gene-Based Analysis;
* TWAS-JTI;
* other gene-level association approaches.

---

# Citation

If you use these scripts, please cite:

----------


---

