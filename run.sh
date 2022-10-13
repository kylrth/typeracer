#!/bin/bash

set -e

USERNAME=$1

# scrape the data into a CSV file
mkdir -p data
python get_csv.py $USERNAME > data/$USERNAME.csv

# generate the individual images
python generate_images.py $USERNAME

# compile the GIF
mkdir -p animated
convert -delay 5 -loop 0 images/$USERNAME/*.jpg \
    -delay 100 images/$USERNAME/$(ls -1 images/$USERNAME | tail -n 1) \
    animated/$USERNAME.gif
