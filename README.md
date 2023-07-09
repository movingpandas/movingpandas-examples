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

### Initialize DVC 

In the ``0-opengeohub-session\start`` directory, run:

```
(mpd-opengeohub2023) PS D:\Documents\GitHub\movingpandas-examples\0-opengeohub-session\solution> dvc init --subdir
Initialized DVC repository.
```

This will create a ``.dvc`` directory and a ``.dvcignore`` file.


### Download a dataset

```
dvc get https://github.com/movingpandas/movingpandas-examples data/boat-positions.csv -o data\boat-positions.csv
```

### Start tracking the dataset

Let's track the ``data\boat-positions.csv`` file: 

```
(mpd-opengeohub2023) PS D:\Documents\GitHub\movingpandas-examples\0-opengeohub-session\solution> dvc add .\data\boat-positions.csv
100% Adding...|██████████████████████████████████████████████████████████████████████████████████████████████████████████|1/1 [00:00,  4.29file/s]
```

To track the changes with git, run:

```
git add 'data\.gitignore' 'data\boat-positions.csv.dvc'
```

To enable auto staging, run:

```
dvc config core.autostage true
```

Let's check the status:

```
(mpd-opengeohub2023) PS D:\Documents\GitHub\movingpandas-examples\0-opengeohub-session\solution> dvc status
Data and pipelines are up to date.
```


### Modify the dataset

Let's clean up the column names. Change the header in ``data\boat-positions.csv`` to 

```
id,t,lon,lat
```

Save the changes and let's check the dvc status again: 

```
(mpd-opengeohub2023) PS D:\Documents\GitHub\movingpandas-examples\0-opengeohub-session\solution> dvc status
data\boat-positions.csv.dvc:
        changed outs:
                modified:           data\boat-positions.csv
```

Save the changes and let's check the dvc status again: 

```
(mpd-opengeohub2023) PS D:\Documents\GitHub\movingpandas-examples\0-opengeohub-session\solution> dvc commit
outputs ['data\\boat-positions.csv'] of stage: 'data\boat-positions.csv.dvc' changed. Are you sure you want to commit it? [y/n] y
(mpd-opengeohub2023) PS D:\Documents\GitHub\movingpandas-examples\0-opengeohub-session\solution> dvc status
Data and pipelines are up to date.
```

