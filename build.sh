#!/bin/bash

# Remove old build
rm -rf transmedia.egg-info/
rm -rf dist/

# Remove any pyc files
for f in `find . -name '*.pyc'`; do
	rm $f
done

python setup.py sdist

# Clear the pip build cache
for d in `find /var/folders/ -name 'pip-build-*' 2>/dev/null`; do
	rm -rf $d/*
done

sdist=$( ls dist/transmedia-*.tar.gz )
pip install $sdist --no-index -f file://$PWD/dist

PYVERSION=$( cat ~/.pyenv/version )
PYMAJOR=$( echo $PYVERSION | awk -F'.' '{OFS="."; print $1,$2}' )
ls ~/.pyenv/versions/$PYVERSION/lib/python${PYMAJOR}/site-packages/transmedia/

pip uninstall -y transmedia

cd docs
make rtd
