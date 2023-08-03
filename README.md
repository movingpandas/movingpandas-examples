# Welcome to the MovingPandas & DVC Session @ OpenGeoHub 2023!

<img align="right" src="https://movingpandas.github.io/movingpandas/assets/img/movingpandas.png">

The main MovingPandas website is **[movingpandas.org](http://movingpandas.org)**

## Preparation study materials

This session requires a basic understanding of Python and Git. Furthermore, to be prepared, please check out the following introductory materials:

1. [DVC](dvc.org/) intro https://youtu.be/kLKBcPonMYw 
1. [GeoPandas](https://geopandas.org) intro https://geopandas.org/en/stable/getting_started/introduction.html
2. [MovingPandas](http://movingpandas.org) intro https://youtu.be/qeLQfnpJV1g

## Installation 

If you want to run these examples on your local machine, use the environment definition file (environment.yml) provided in this repository.

### Preparation 

Make sure that you have a command line interface that can run GIT and conda/mamba commands: 

1. Install git
1. Install miniconda: https://conda.io/projects/conda/en/latest/user-guide/install/index.html 
1. Install mamba in the base conda environment: `conda install -c conda-forge mamba` (optional, but recommended because mamba is much faster at solving the dependencies than conda)

And as an IDE, I recommend VSCode due to its GIT and DVC integration

1. Install VSCode: https://code.visualstudio.com/Download 

### MovingPandas environment

1. Clone the movingpandas-examples repository
1. Switch to the opengeohub2023 branch: `git checkout opengeohub2023`
1. Create the environment: `mamba env create -f environment.yml` (or `conda env create -f environment.yml` if you didn't install mamba)
1. Activate the environment: `conda activate mpd-opengeohub2023`
