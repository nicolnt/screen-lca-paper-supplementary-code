# Read me

## Related publication

If you utilize any portions of the code, results, or draw inspiration for your projects, please give proper credit by citing the published article below.

 - Title: Residual biomass to bio-based chemicals and plastics: ex-ante screening methodology for prioritizing high-impact substitutions
 - Authors: [Nicolas LIENART](https://orcid.org/0009-0001-3259-2819), [Thibaut LECOMPTE](https://orcid.org/0000-0001-9237-8454), [Lorie HAMELIN](https://orcid.org/0000-0001-9092-1900) 
 - Journal: Resources, Conservation and Recycling (RCR) - Elsevier
 - Doi: #todo
 - Git repository (Forge INRAE): https://forge.inrae.fr/nicolas.lienart/screen-lca-paper-supplementary-code
 - Git repository (GitHub): https://github.com/nicolnt/screen-lca-paper-supplementary-code

## Notebook files

They can be read directly (non-interactively) from Gitlab or Github in there rendered form. Links to notebooks listed in alphabetical order:

 - [Calculate product footprints and generate hotspot figure.ipynb](<./Python_notebooks/Calculate hotspot products footprints and contributions.ipynb>)
 - [Calculate sectors footprint with EXIOBASE.ipynb](<./Python_notebooks/Calculate sectors footprint with EXIOBASE.ipynb>)
 - [Convert PRODCOM codes to Harmonized System (HS) 2022 codes.ipynb](<./Python_notebooks/Convert PRODCOM codes to Harmonized System (HS) 2022 codes.ipynb>)
 - [Extract PRODCOM data.ipynb](<./Python_notebooks/Extract PRODCOM data.ipynb>)
 - [Generate main paper hotspot figure 2.ipynb](<./Python_notebooks/Generate main paper hotspot figure 2.ipynb>)
 - [Get product importers from BACI and Ecoinvent geographies.ipynb](<./Python_notebooks/Get product importers from BACI and Ecoinvent geographies.ipynb>)

## Structure

```
.
├── Article_data/
│   ├── Step 2 results from Exiobase data manipulations.xlsx
│   ├── Step 3 results from Prodcom data manipulations.xlsx
│   └── Step 4 hotspot figure data.xlsx
├── BACI_data/
│   └── BACI_HS22_V202501/
│       ├── BACI_HS22_Y2022_V202501.csv
│       ├── Readme.txt
│       ├── country_codes_V202501.csv
│       └── product_codes_HS22_V202501.csv
├── Ecoinvent_data/
│   └── Ecoinvent all locations - v2.5 - allgeos.csv
├── EXIOBASE_data/
│   └── EXIOBASE_v3.10.2/
│       └── IOT_2022_pxp/
│           └── (... Extracted Exiobase files)
├── Kumu_data/
│   ├── kumu-nicolas-lienart-screenlca-paper-biobased-pathways.json
│   └── kumu-nicolas-lienart-screenlca-paper-biobased-pathways.xlsx
├── PRODCOM_data/
│   ├── CN2024_PRODCOM2024-export.jsonld
│   ├── ESTAT_GEO_27.0.tsv
│   ├── HS classification based on CN2024.csv
│   ├── ds-059358__custom_19869966_spreadsheet.xlsx
│   ├── estat_ds-059358.tsv
├── Python_notebooks/
│   ├── Calculate hotspot products footprints and contributions.ipynb
│   ├── Calculate sectors footprint with EXIOBASE.ipynb
│   ├── Convert PRODCOM codes to Harmonized System (HS) 2022 codes.ipynb
│   ├── Extract PRODCOM data.ipynb
│   ├── Generate main paper hotspot figure 2.ipynb
│   └── Get product importers from BACI and Ecoinvent geographies.ipynb
├── Python_utils/
│   ├── __init__.py
│   └── ecoinvent_databases.py
├── Output_data/
│   └── (... intermediate and final outputs will go here)
├── LICENSE.txt
├── README.md
└── environment.yml
```

Some of the files presented here are not included due to licencing or size constraints (e.g., BACI, EXIOBASE). The user is invited to follow the relevant procedures to obtain them via the official sources ([See "Download missing data"](#Download-missing-data) or links provided in the Python notebooks).

## Setup Repository

Clone this repository:

```bash
git clone https://forge.inrae.fr/nicolas.lienart/screen-lca-paper-supplementary-code/ --depth=1
```

## Setup Python Environment

Set up a Python virtual environment that includes all packages required to build the documentation. A [Conda environment file](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) is provided [for convenient setup](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file). The file is located at [``./environment.yml``](environment.yml). You can replace the environment name `lienart_etal_2026-screenlca-paper-si-code`. Install the environment by running from the repository root directory:

```bash
conda env create -f 'environment.yml' --name 'lienart_etal_2026-screenlca-paper-si-code'
```

and activate the environment:

```bash
conda activate 'lienart_etal_2026-screenlca-paper-si-code'
```

## Kumu database

Interactive pathway database available at https://kumu.io/nicolas-lienart/screenlca-paper-biobased-pathways

Raw JSON and Excel database files are available in the [`Kumu_data/`](<./Kumu_data/>) directory.

## Download missing data

### EXIOBASE

EXIOBASE 3 | Published May 13, 2026 | Version 3.10.2
Dataset link: https://zenodo.org/records/20051562

### BACI

Get BACI data here: https://www.cepii.fr/DATA_DOWNLOAD/baci/doc/baci_webpage.html

### PRODCOM

- Repository link: https://ec.europa.eu/eurostat/databrowser/bulk?lang=en&alphabeticalFilter=D&searchFilter=DS
- Reporter regions of PRODCOM download link: https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/codelist/ESTAT/geo?format=TSV

### Classification code correspondence

#### PRODCOM code ↔ 6-digit Harmonized System (HS) 2022

Get the JSON-LD correspondence file from EU ShowVoc platform: https://showvoc.op.europa.eu/#/datasets/ESTAT_Combined_Nomenclature__2024__CN_2024/unknown/data

(Combined Nomenclature, 2024 (CN 2024)) - "UNKNOWN (ESTAT_Combined_Nomenclature,_2024_(CN_2024))"

Correspondences tab > CN2024_PRODCOM2024 > Download (JSON-LD) and save it to `Prodcom_data/CN2024_PRODCOM2024-export.jsonld`

## Licence

This work is licenced under the Creative Commons Attribution (CC-BY 4.0) public licence.

See the licence file: [LICENSE.txt](<LICENSE.txt>)