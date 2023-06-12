#!/usr/bin/env python3

from setuptools import setup, Extension

setup(
    name='tosti',

    version='0.0.1',

    # List of dependencies
    install_requires=[
        'llvmlite',
    ],

    ext_package = 'tosti',
    ext_modules=[
        Extension('_sim', ['src/tosti.c']),
    ],
)
