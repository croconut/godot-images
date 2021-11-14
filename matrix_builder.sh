#!/bin/bash -e

pip install beautifulsoup4 requests

values=$(python ./download_all.py)
echo "::set-output name=version_matrix::${values}"