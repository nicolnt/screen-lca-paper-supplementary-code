# Read me

## Related publication

 - Title: Residual biomass to bio-based chemicals and plastics: ex-ante screening methodology for prioritizing high-impact substitutions
 - Authors: [Nicolas LIENART](https://orcid.org/0009-0001-3259-2819), [Thibaut LECOMPTE](https://orcid.org/0000-0001-9237-8454), [Lorie HAMELIN](https://orcid.org/0000-0001-9092-1900) 
 - Journal: Resources, Conservation and Recycling (RCR) - Elsevier
 - Doi: #todo
 - Git repository (Forge INRAE): https://forge.inrae.fr/nicolas.lienart/screen-lca-paper-supplementary-code
 - Git repository (GitHub): https://github.com/nicolnt/screen-lca-paper-supplementary-code

## Notebook files

They can be read directly from Gitlab or Github in there rendered form.

 - [Sectors footprint with Exiobase.ipynb](<./Sectors footprint with Exiobase.ipynb>)
 - [Extract Prodcom data.ipynb](<./Extract Prodcom data.ipynb>)
 - [Calculate product footprints and generate hotspot figure.ipynb](<./Calculate product footprints and generate hotspot figure.ipynb>)

## Structure

```
.
├── Article_data/
│   ├── Step 2 results from Exiobase data manipulations.xlsx
│   ├── Step 3 results from Prodcom data manipulations.xlsx
│   └── Step 4 hotspot figure data.xlsx
├── Exiobase_data/
│   └── EXIOBASE_v3.9.5/
│       └── IOT_2019_pxp/
│           └── (... Extracted Exiobase files)
├── Kumu_data/
│   ├── kumu-nicolas-lienart-screenlca-paper-biobased-pathways.json
│   └── kumu-nicolas-lienart-screenlca-paper-biobased-pathways.xlsx
├── Prodcom_data/
│   ├── 20260326 - data input.csv
│   ├── ESTAT_GEO_27.0.tsv
│   ├── ds-059358__custom_19869966_spreadsheet.xlsx
│   ├── estat_ds-059358.tsv
├── output/
│   └── (... code intermediate and final outputs will go here)
├── Calculate product footprints and generate hotspot figure.ipynb
├── Extract Prodcom data.ipynb
├── LICENSE.txt
├── README.md
├── Sectors footprint with Exiobase.ipynb
└── environment.yml
```

## Setup Repository

1. Clone this repository:

```bash
git clone https://forge.inrae.fr/nicolas.lienart/screen-lca-paper-supplementary-code/ --depth=1
```

2. Initialize (=download) the submodules (`brightway-2-analyzer`, `brightway2-calc`, etc.):

```bash
git submodule update --init --recursive --remote --force
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

Raw JSON and Excel database files are available in the [`Kumu_data/`](.Kumu_data/) directory.