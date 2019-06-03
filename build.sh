#!/bin/bash

# check parameter passed in
if [ "$#" -ne 1 ]; then
    echo "Illegal number of parameters: only version number required."
    exit
fi

# Remove existing package resources.
rm -r dist
rm -r build
rm -r lepmlutils.egg-info

# Replace version number with argument.
echo "$1"
sed -i "s/version.*/version='$1',/" setup.py

# Build new package resources.
python setup.py bdist_wheel 
python setup.py sdist

exit