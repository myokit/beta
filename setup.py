#!/usr/bin/env python3

from setuptools import find_packages, setup, Extension


# Load text for description and license
with open('README.md') as f:
    readme = f.read()


setup(
    name='myokit_beta',

    # Version
    version='0.0.2',

    # Description
    description='Trying out distribution of wheels etc and llvm',
    long_description=readme,
    long_description_content_type='text/markdown',

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
