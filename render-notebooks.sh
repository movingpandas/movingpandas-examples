#!/bin/bash

# execute + export all notebooks to HTML
for nb in **/*.ipynb; do
  jupyter nbconvert --to html --execute "$nb" \
    --output-dir ./html-output \
    --ExecutePreprocessor.timeout=600
done



# jupyter nbconvert --to html --execute "12-ogc-moving-features.ipynb" --output-dir ./html-output --ExecutePreprocessor.timeout=600