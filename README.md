# Welcome to the MovingPandas examples repository!

<a href="https://codeberg.org/movingpandas/movingpandas-examples">
    <img alt="Get it on Codeberg" src="https://get-it-on.codeberg.org/get-it-on-blue-on-white.png" height="60" align="right">
</a>

[![Issue Tracker](https://img.shields.io/badge/Issue_tracker-Codeberg-blue.svg)](https://codeberg.org/movingpandas/movingpandas-examples/issues) 

This repository contains Jupyter notebooks demonstrating MovingPandas features.

<img align="right" src="https://movingpandas.github.io/movingpandas/assets/img/movingpandas.png"  width="200">

👉 **Jump right in with [Example 1: Getting Started](https://movingpandas.github.io/movingpandas-website/1-tutorials/1-getting-started.html)**

You can run the these notebooks on MyBinder - no installation required: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/movingpandas/movingpandas-examples/main)

Alternatively, if you prefer VS Code, you can run Github Codespaces: 
[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/movingpandas/movingpandas-examples)

The main MovingPandas repo is https://github.com/movingpandas/movingpandas

Visit **[movingpandas.org](http://movingpandas.org)** for details! 

## Installation 

If you want to run these examples on your local machine, use the environment definition file (environment.yml) provided in this repository.

1. Install Conda and mamba 
1. Clone the movingpandas-examples repository
1. Navigate to the cloned directory
1. Run `mamba env create -f environment.yml`


## Post installation

1. Activate the `mpd-ex` environment
1. Launch Jupyter notebooks and navigate to the `movingpandas-examples` directory 
1. Now you can run the notebooks, experiment with the code and adjust it to your own data

## Generating html exports using nbautoexport

First, you will need to install nbautoexport. Then register nbautoexport to run automatically while using Jupyter Notebook or Jupyter Lab:

1. conda install nbautoexport --channel conda-forge
1. nbautoexport install

Finally restart the Jupyter server. 

