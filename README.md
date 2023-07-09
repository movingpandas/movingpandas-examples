# Welcome to the MovingPandas & DVC Session @ OpenGeoHub 2023!

<img align="right" src="https://movingpandas.github.io/movingpandas/assets/img/movingpandas.png">

The main MovingPandas website is **[movingpandas.org](http://movingpandas.org)**

## Preparation study materials

This session requires a basic understanding of Python and Git. Furthermore, to be prepared, please check out the following introductory materials:

1. [DVC](dvc.org/) intro https://youtu.be/kLKBcPonMYw 
1. [GeoPandas](https://geopandas.org) intro https://geopandas.org/en/stable/getting_started/introduction.html 

## Installation 

If you want to run these examples on your local machine, use the environment definition file (environment.yml) provided in this repository.

### Preparation (conda/mamba)

1. Install git
1. Install miniconda: https://conda.io/projects/conda/en/latest/user-guide/install/index.html 
1. Install mamba: `conda install -c conda-forge mamba` (optional, but recommended because mamba is much faster at solving the dependencies than conda)
1. Install VSCode: https://code.visualstudio.com/Download (optional, but recommended due to its DVC integration)

### MovingPandas environment

1. Clone the movingpandas-examples repository
1. Switch to the opengeohub2023 branch: `git checkout opengeohub2023`
1. Create the environment: `mamba env create -f environment.yml` (or `conda env create` if you didn't install mamba)
1. Activate the environment: `conda activate mpd-opengeohub2023`


## Getting started

```
(mpd-opengeohub2023) PS D:\Documents\GitHub\movingpandas-examples\0-opengeohub-session\solution> dvc init --subdir
Initialized DVC repository.
```

