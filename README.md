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


## Getting started

### Initialize DVC 

In the ``0-opengeohub-session\start`` directory, run:

```
dvc init --subdir
```

This will create a ``.dvc`` directory and a ``.dvcignore`` file and you should see the output:

```
Initialized DVC repository.

You can now commit the changes to git.
```


### Download a dataset

```
dvc get https://github.com/movingpandas/movingpandas-examples data/boat-positions.csv -o data\boat-positions.csv
```

### Start tracking the dataset

Let's track the ``data\boat-positions.csv`` file: 

```
dvc add .\data\boat-positions.csv
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
dvc status
```

This should output:

```
Data and pipelines are up to date.
```

Finally, let's commit the initialized DVC setup to git:

```
git commit -m "Add dvc"
```

As a confirmation, this will display the new dvc configuration files, including the `boat-positions.csv.dvc` which is the placeholder for our dataset. Instead of pushing the whole dataset to the git repo, only the placeholder is include. This ensures that the git repo is not flooded with (potentially huge) datasets: 

```
[opengeohub2023 a59662e] Add dvc
 5 files changed, 12 insertions(+)
 create mode 100644 0-opengeohub-session/start/.dvc/.gitignore
 create mode 100644 0-opengeohub-session/start/.dvc/config
 create mode 100644 0-opengeohub-session/start/.dvcignore
 create mode 100644 0-opengeohub-session/start/data/.gitignore
 create mode 100644 0-opengeohub-session/start/data/boat-positions.csv.dvc
```



### Modify the dataset

Let's clean up the column names. Change the header in ``data\boat-positions.csv`` to 

```
id,t,lon,lat
```

Save the changes and let's check the dvc status again: 

```
dvc status
```

This will output:
```
data\boat-positions.csv.dvc:
        changed outs:
                modified:           data\boat-positions.csv
```

Let's commit our changes to dvc:

```
dvc commit
```

This will as for our confirmation

```
outputs ['data\\boat-positions.csv'] of stage: 'data\boat-positions.csv.dvc' changed. Are you sure you want to commit it? [y/n] 
```

When we check the dvc status again:

```
dvc status
```

We now get:

```
Data and pipelines are up to date.
```

This means we can commit the new ``data\boat-positions.csv.dvc`` to git:

```
git commit -m "Update header"
```

### Undoing changes 

To revert our changes and go back to the previous file version, run:

```
git checkout HEAD~1 .\data\boat-positions.csv.dvc
dvc checkout
```

Which will show that the csv file has been modified:

```
M       data\boat-positions.csv
```

Checking the dvc status:

```
dvc status
```

Shows:

```
Data and pipelines are up to date.
```

When we look at the .csv file now, the header has reverted back to the original.

To return to the latest version with our nice short column names, change `HEAD~1` to `HEAD` and run:

```
git checkout HEAD .\data\boat-positions.csv.dvc
dvc checkout
```

Which will again confirm that the csv has been changed:

```
M       data\boat-positions.csv
```

To find the correct version of a file, we can have a look at the git commit log: 

```
git log --oneline
```

Which outputs the log similar to: 

```
ab17c8f (HEAD -> opengeohub2023) Update header
207a496 Add dvc
```

You may also use the hash (e.g. `207a496` instead of `HEAD~1`) to access a specific commit directly. 


