#!/usr/bin/env python3

from setuptools import find_packages, setup, Extension

setup(
    name='myokit_beta',

    version='0.0.1',

    # Packages to include
    packages=find_packages(include=('myokit_beta', 'myokit_beta.*')),

    # List of dependencies
    install_requires=[
        'llvmlite',
    ],

    #ext_package = 'tosti',
    ext_modules=[
        Extension('myokit_beta._sim.sim1', ['src/sim1.c']),
    ],
)
