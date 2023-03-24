#!/bin.sh

# clear cache
find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf

# install
pip install --upgrade setuptools wheel
python setup.py sdist bdist_wheel
pip install --upgrade twine
twine upload dist/*

# clear
rm -rf chat_agent.egg-info
rm -rf build
rm -rf dist