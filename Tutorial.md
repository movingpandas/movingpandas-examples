# Welcome to the MovingPandas & DVC Session @ OpenGeoHub 2023!

<img align="right" src="https://movingpandas.github.io/movingpandas/assets/img/movingpandas.png">

[OpenGeoHub Summer School 2023 - Session: Data engineering for Mobility Data Science (with Python and DVC)](
https://pretalx.earthmonitor.org/opengeohub-summer-school-2023/talk/YKZKSA/)

This tutorial relies heavily on [DVC](http://dvc.org) and [MovingPandas](http://movingpandas.org).


## Setup 

Make sure to follow the instructions in the [README.md](README.md) to set up your Python environment. 

This tutorial consists of two main parts: 

1. Tracking datasets with DVC
1. Tracking analysis workflows with DVC pipelines


## Tracking datasets

In this first part, we will initialize DVC and configure it to keep track of our mobilty dataset. 


### Initializing DVC 

To initialize DVC in the ``0-opengeohub-session\start`` directory, run:

```
dvc init --subdir
```

This will create a ``.dvc`` directory and a ``.dvcignore`` file and you should see the output:

```
Initialized DVC repository.

You can now commit the changes to git.
```


### Downloading a dataset

Next, we will download our tutorial dataset, a CSV file containing boat locations: 

```
dvc get https://github.com/movingpandas/movingpandas-examples data/boat-positions.csv -o data\boat-positions.csv
```

### Start tracking the dataset

Let's track the ``data\boat-positions.csv`` file: 

```
dvc add .\data\boat-positions.csv
```

To track the changes with GIT, run:

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

Finally, let's commit the initialized DVC setup to GIT:

```
git commit -m "Add dvc"
```

As a confirmation, this will display the new DVC configuration files, including the `boat-positions.csv.dvc` which is the placeholder for our dataset. Instead of pushing the whole dataset to the GIT repo, only the placeholder is included. This ensures that the GIT repo is not flooded with (potentially huge) datasets: 

```
[opengeohub2023 a59662e] Add dvc
 5 files changed, 12 insertions(+)
 create mode 100644 0-opengeohub-session/start/.dvc/.gitignore
 create mode 100644 0-opengeohub-session/start/.dvc/config
 create mode 100644 0-opengeohub-session/start/.dvcignore
 create mode 100644 0-opengeohub-session/start/data/.gitignore
 create mode 100644 0-opengeohub-session/start/data/boat-positions.csv.dvc
```



### Handling dataset modifications

Let's clean up the column names. Change the header in ``data\boat-positions.csv`` to 

```
id,t,lon,lat
```

Save the changes and let's check the DVC status again: 

```
dvc status
```

This will output:
```
data\boat-positions.csv.dvc:
        changed outs:
                modified:           data\boat-positions.csv
```

Let's commit our changes to DVC:

```
dvc commit
```

This will as for our confirmation

```
outputs ['data\\boat-positions.csv'] of stage: 'data\boat-positions.csv.dvc' changed. Are you sure you want to commit it? [y/n] 
```

When we check the DVC status again:

```
dvc status
```

We now get:

```
Data and pipelines are up to date.
```

Next, let's check the GIT status:

```
git status
```

If ``data\boat-positions.csv.dvc`` hasn't been staged for commit automatically, add it manually:

```
git add .\data\boat-positions.csv.dvc
```

Then we can commit the new ``data\boat-positions.csv.dvc`` to GIT:

```
git commit -m "Update header"
```

### Undoing changes 

To revert our changes and go back to the previous file version, run:

```
git checkout HEAD~1 .\data\boat-positions.csv.dvc
dvc checkout
```

Which will show that the CSV file has been modified:

```
M       data\boat-positions.csv
```

Checking the DVC status:

```
dvc status
```

Shows:

```
Data and pipelines are up to date.
```

When we look at the CSV file now, the header has reverted back to the original.

To return to the latest version with our nice short column names, change `HEAD~1` to `HEAD` and run:

```
git checkout HEAD .\data\boat-positions.csv.dvc
dvc checkout
```

Which will again confirm that the CSV has been changed:

```
M       data\boat-positions.csv
```

To find the correct version of a file, we can have a look at the GIT commit log: 

```
git log --oneline
```

Which outputs the log similar to: 

```
ab17c8f (HEAD -> opengeohub2023) Update header
207a496 Add dvc
```

You may also use the hash (e.g. `207a496` instead of `HEAD~1`) to access a specific commit directly. 


## Setting up a data pipeline

For this tutorial, we will implement a stop extraction analysis using MovingPandas. For the development of this analysis from scratch, head over to `solution/notebook.ipynb`.

After we have decided how our analysis should  work, we can automate it and track it using a DVC data pipeline. 

To do so, first, we need a script that implements the data processing: 


### Creating a first analysis script

Let's create a small analysis script called ``extract-stops.py`` that extracts stops from the boat trajectories:

```
import pandas as pd 
import movingpandas as mpd
from datetime import timedelta

def run():
    print("Reading data ...")
    df = pd.read_csv("./data/boat-positions.csv", sep=",")
    df['t'] = pd.to_datetime(df['t'], format='%d/%m/%Y %H:%M')
    print("Creating trajectories ...")
    tc = mpd.TrajectoryCollection(df, traj_id_col="id", t="t", x="lon", y="lat")
    print("Extracting stops ...")
    stop_detector = mpd.TrajectoryStopDetector(tc, n_threads=3)
    stops = stop_detector.get_stop_points(max_diameter=1000, min_duration=timedelta(hours=1))
    print(stops)
    print("Saving results ...")
    stops.to_file('stops.geojson', driver='GeoJSON')
    print("SUCCESS! Created output stops.geojson")

if __name__ == '__main__':
    run()
```

When we run the script using:

```
python .\extract-stops.py
```

This should output:

```
Reading data ...
Creating trajectories ...
Extracting stops ...
                                          geometry          start_time            end_time  traj_id  duration_s
stop_id
2_2021-03-21 08:29:00    POINT (32.35567 31.21248) 2021-03-21 08:29:00 2021-03-21 23:11:00        2     52920.0
3_2021-03-24 04:15:00    POINT (32.33328 31.42789) 2021-03-24 04:15:00 2021-03-24 06:24:00        3      7740.0
4_2021-03-23 22:23:00    POINT (32.32796 31.39507) 2021-03-23 22:23:00 2021-03-24 12:46:00        4     51780.0
5_2021-03-20 10:15:00    POINT (32.35727 31.21790) 2021-03-20 10:15:00 2021-03-21 03:55:00        5     63600.0
6_2021-03-23 23:59:00    POINT (32.39495 30.34766) 2021-03-23 23:59:00 2021-03-24 02:26:00        6      8820.0
...                                            ...                 ...                 ...      ...         ...
250_2021-03-23 17:17:00  POINT (32.53383 29.83297) 2021-03-23 17:17:00 2021-03-24 12:21:00      250     68640.0
251_2021-03-23 22:21:00  POINT (32.35181 31.45093) 2021-03-23 22:21:00 2021-03-24 12:48:00      251     52020.0
252_2021-03-20 00:24:00  POINT (32.32610 31.45075) 2021-03-20 00:24:00 2021-03-20 02:54:00      252      9000.0
255_2021-03-23 08:52:00  POINT (32.57538 29.85072) 2021-03-23 08:52:00 2021-03-24 11:14:00      255     94920.0
256_2021-03-20 00:25:00  POINT (32.32908 31.19485) 2021-03-20 00:25:00 2021-03-24 12:35:00      256    389400.0

[318 rows x 5 columns]
Saving results ...
SUCCESS! Created output stops.geojson
```


### Configuring our first pipeline stage

Now, we can configure DVC to run our script. To do that, we create a DVC stage with the name `stop-extraction` that uses our Python script and the CSV data to create the stop.geojson: 

```
dvc stage add -n stop-extraction -d extract-stops.py -d data/boat-positions.csv -o stops.geojson python extract-stops.py
```

Which will be confirmed by 

```
Added stage 'stop-extraction' in 'dvc.yaml'
```


*For more info check https://dvc.org/doc/start/data-management/data-pipelines#pipeline-stages*


The `dvc.yaml` should now look like this:

```
stages:
  stop-extraction:
    cmd: python extract-stops.py
    deps:
    - data/boat-positions.csv
    - extract-stops.py
    outs:
    - stops.geojson
```

To run our new pipeline, we use the repro command:

```
dvc repro
```

Which will execute our one-stage pipeline:

```
'data\boat-positions.csv.dvc' didn't change, skipping
Running stage 'stop-extraction':
> python extract-stops.py
Reading data ...
Creating trajectories ...
Extracting stops ...
                                          geometry          start_time            end_time  traj_id  duration_s
stop_id
2_2021-03-21 08:29:00    POINT (32.35567 31.21248) 2021-03-21 08:29:00 2021-03-21 23:11:00        2     52920.0
3_2021-03-24 04:15:00    POINT (32.33328 31.42789) 2021-03-24 04:15:00 2021-03-24 06:24:00        3      7740.0
4_2021-03-23 22:23:00    POINT (32.32796 31.39507) 2021-03-23 22:23:00 2021-03-24 12:46:00        4     51780.0
5_2021-03-20 10:15:00    POINT (32.35727 31.21790) 2021-03-20 10:15:00 2021-03-21 03:55:00        5     63600.0
6_2021-03-23 23:59:00    POINT (32.39495 30.34766) 2021-03-23 23:59:00 2021-03-24 02:26:00        6      8820.0
...                                            ...                 ...                 ...      ...         ...
250_2021-03-23 17:17:00  POINT (32.53383 29.83297) 2021-03-23 17:17:00 2021-03-24 12:21:00      250     68640.0
251_2021-03-23 22:21:00  POINT (32.35181 31.45093) 2021-03-23 22:21:00 2021-03-24 12:48:00      251     52020.0
252_2021-03-20 00:24:00  POINT (32.32610 31.45075) 2021-03-20 00:24:00 2021-03-20 02:54:00      252      9000.0
255_2021-03-23 08:52:00  POINT (32.57538 29.85072) 2021-03-23 08:52:00 2021-03-24 11:14:00      255     94920.0
256_2021-03-20 00:25:00  POINT (32.32908 31.19485) 2021-03-20 00:25:00 2021-03-24 12:35:00      256    389400.0

[318 rows x 5 columns]
Saving results ...
SUCCESS! Created output stops.geojson
Generating lock file 'dvc.lock'
Updating lock file 'dvc.lock'
Use `dvc push` to send your updates to remote storage.
```


Note that if we run `dvc repro` a second time, we get:

```
'data\boat-positions.csv.dvc' didn't change, skipping
Stage 'stop-extraction' didn't change, skipping
Data and pipelines are up to date.
```

This means that DVC knows that neither the input data nor the analysis script changed and, therefore, it is not necessary to re-run the stage. 

When we run `git status`, we see changes to DVC files and we are notified that we still need to add extract-stops.py to GIT:

```
On branch opengeohub2023-wip
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   .gitignore
        new file:   dvc.lock
        new file:   dvc.yaml

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        extract-stops.py
```

So let's add ``extract-stops.py`` and commit our changes.

```
git add extract-stops.py
git commit -m "First stage"
```


### Making changes to the analysis script:

Next, let's remove to noisy ``print(stops)`` statement from our script. When we save the changes and run `dvc status`, we see:

```
stop-extraction:
        changed deps:
                modified:           extract-stops.py
```

Now, if we run `dvc repro` again, the stop-extraction stage is executed again:

```
'data\boat-positions.csv.dvc' didn't change, skipping
Running stage 'stop-extraction':
> python extract-stops.py
Reading data ...
Creating trajectories ...
Extracting stops ...
Saving results ...
SUCCESS! Created output stops.geojson
Updating lock file 'dvc.lock'
Use `dvc push` to send your updates to remote storage.
```

Again, let's commit our changes to GIT:

```
git add extract-stops.py
git commit -m "Remov print"
```


### Making changes to the input data


If we make a change to the CSV file, ``dvc status`` will tell us: 

```
stop-extraction:
        changed deps:
                modified:           data\boat-positions.csv
data\boat-positions.csv.dvc:
        changed outs:
                modified:           data\boat-positions.csv
```

Since DVC recognizes this change, ``dvc repro`` will know that it has to run the stage with the changed input data:

```
Verifying data sources in stage: 'data\boat-positions.csv.dvc'

Running stage 'stop-extraction':
> python extract-stops.py
Reading data ...
Creating trajectories ...
Extracting stops ...
Saving results ...
SUCCESS! Created output stops.geojson
Updating lock file 'dvc.lock'
Use `dvc push` to send your updates to remote storage.
```

And ``git status`` will show us that the lock file and the CSV placeholder have been changed:

```
On branch opengeohub2023-wip
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   data/boat-positions.csv.dvc
        modified:   dvc.lock
```

Let's commit this:

```
git commit -m "Data change"
```

Our GIT log now looks somting like this:

```
git log --oneline

98a9db2 (HEAD -> opengeohub2023-wip) Data change
b04a4cc Remove print
96b89cb First stage
e3148a2 Update header
6ff13e0 Add dvc
```

### Reverting changes

If we now decide to revert the changes in our CSV file and run ``dvc repro`` again, we get:

```
Verifying data sources in stage: 'data\boat-positions.csv.dvc'

Stage 'stop-extraction' is cached - skipping run, checking out outputs
Updating lock file 'dvc.lock'
Use `dvc push` to send your updates to remote storage.
```

Which means that DVC realized that we already computed these results previously and that it can extract them from its cache. This can save a lot of time, when we work with time-intensive analyses. 

``git status`` shows that only the lock and placeholder files have changed: 

```
On branch opengeohub2023-wip
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   data/boat-positions.csv.dvc
        modified:   dvc.lock
```

