# -*- coding: utf-8 -*-

# This file is part of GeoSmoothing.
# https://github.com/GeographicaGS

# Licensed under the GPLv2 license:
# https://www.gnu.org/licenses/gpl-2.0.txt
# Copyright (c) 2016, Cayetano Benavent <cayetano.benavent@geographica.gs>

from setuptools import setup, find_packages


# Get the long description from README file.
# Before upload a new version run rstgenerator.sh
# to update Readme reStructuredText file from
# original Readme markdown file.
with open('README.rst', 'r') as f:
    long_description = f.read()

setup(
    name='geosmoothing',
    version='0.1',

    description='Smoothing GIS features with B-Splines. Input formats are WKT and SHP. Builded on top of Numpy, Scipy, Shapely and Fiona.',
    long_description=long_description,

    author='Cayetano Benavent',
    author_email='cayetano.benavent@geographica.gs',

    scripts=['bin/geosmoothing_shp','bin/geosmoothing_wkt'],

    # The project's main homepage.
    url='http://github.com/GeographicaGS/GeoSmoothing',

    # Licensed under the GPLv2 license:
    # https://www.gnu.org/licenses/gpl-2.0.txt
    license='GPLv2',

    # According to: https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Programming Language :: Python :: 2.7',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: GIS'
    ],

    keywords='vector GIS smoothing spline',

    packages=find_packages(),
    include_package_data=False,
    install_requires=[
        'numpy',
        'scipy',
        'fiona',
        'shapely'

    ]

)
