# Welcome to the MovingPandas examples repository!

<img align="right" src="https://movingpandas.github.io/movingpandas/assets/img/movingpandas.png">

This repository contains Jupyter notebooks demonstrating MovingPandas features.

👉 **Jump right in with [Example 1: Getting Started](https://github.com/movingpandas/movingpandas-examples/blob/main/1-tutorials/1-getting-started.ipynb)**

You can run the these notebooks on MyBinder - no installation required: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/anitagraser/movingpandas-examples/main)

The main MovingPandas repo is https://github.com/anitagraser/movingpandas

Visit **[movingpandas.org](http://movingpandas.org)** for details! 

## Installation 

If you want to run these examples on your local machine, use the environment definition file (environment.yml) provided in this repository.

1. Clone the movingpandas-examples repository
1. Install Conda (command line interface) or Anaconda (graphical user interface) and continue with the instructions in the corresponding section

### Using conda

1. Navigate to the cloned directory
1. Run `conda env create -f environment.yml`

### Using Anaconda

1. In Anaconda Navigator | Environments | Import select the movingpandas-experiments environment.yml from the cloned directory

## Post installation

1. Activate the `mpd-ex` environment
1. Launch Jupyter notebooks and navigate to the `movingpandas-examples` directory 
1. Now you can run the notebooks, experiment with the code and adjust it to your own data

## Generating html exports using nbautoexport

First, you will need to install nbautoexport. Then register nbautoexport to run automatically while using Jupyter Notebook or Jupyter Lab:

1. conda install nbautoexport --channel conda-forge
1. nbautoexport install

Finally restart the Jupyter server. 

