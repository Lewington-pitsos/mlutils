#!/bin/bash

rm -r dist
rm -r build
rm -r lepmlutils.egg-info
python setup.py bdist_wheel 
python setup.py sdist

exit