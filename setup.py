#!/usr/bin/env python3

from setuptools import find_packages, setup, Extension

setup(
    name='tosti',

    version='0.0.1',

    # Packages to include
    packages=find_packages(include=('tosti', 'tosti.*')),

    # List of dependencies
    install_requires=[
        'llvmlite',
    ],

    #ext_package = 'tosti',
    ext_modules=[
        Extension('tosti._sim', ['src/tosti.c']),
    ],
)
