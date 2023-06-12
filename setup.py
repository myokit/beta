#!/usr/bin/env python3

from setuptools import setup, Extension

setup(
    name='tosti',

    version='0.0.1',

    install_requires=[
    ],

    # List of dependencies
    install_requires=[
        'llvmlite',
    ],

    ext_modules=[
        Extension(
            name="tosti",
            sources=['src/tosti.c'],
        ),
    ],
)
