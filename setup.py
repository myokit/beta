#!/usr/bin/env python3
import platform

from setuptools import find_packages, setup, Extension


# Load text for description and license
with open('README.md') as f:
    readme = f.read()


# Package data (will be refined below)
sdist_only_data = ['myokit_beta/_sim/*']
bdist_only_data = []


# Platform differences
system = platform.system()
if system == 'Windows':
    sundials_inc = ['./ext-inc/sundials-win-vs']
    sundials_lib = ['./ext-lib/sundials-win-vs']
    bdist_only_data.extend(sundials_lib)
elif system == 'Darwin':
    sundials_inc = [
        '/usr/local/include',
        '/opt/local/include',
        '/opt/homebrew/include',
    ]
    sundials_lib = [
        '/usr/local/lib',
        '/usr/local/lib64',
        '/opt/local/lib',
        '/opt/local/lib64',
        '/opt/homebrew/lib',
        '/opt/homebrew/lib64',
    ]
else:
    sundials_inc = [
        '/usr/local/include',
        '/opt/local/include',
    ]
    sundials_lib = [
        #'/usr/local/lib',
        #'/usr/local/lib64',
        #'/opt/local/lib',
        #'/opt/local/lib64',
    ]


# CVODES Simulation
sim_libraries = ['sundials_cvodes', 'sundials_nvecserial']
if system != 'Windows':
    sim_libraries.append('m')
cvodes_sim = Extension(
    'myokit_beta._sim._cvodessim_ext',
    sources=['myokit_beta/_sim/_cvodessim.c'],
    libraries=sim_libraries,
    library_dirs=sundials_lib,
    include_dirs=sundials_inc,
    #runtime_library_dirs=runtime,
)



# Go!
setup(
    name='myokit_beta',

    # Version
    version='0.0.6',

    # Description
    description='Trying out distribution of wheels etc and llvm',
    long_description=readme,
    long_description_content_type='text/markdown',

    # Packages to include
    packages=find_packages(include=('myokit_beta', 'myokit_beta.*')),

    # Include non-python files
    # https://setuptools.pypa.io/en/latest/userguide/datafiles.html
    # https://sinoroc.gitlab.io/kb/python/package_data.html
    # To package with sdist and bdist: add to MANIFEST.in
    include_package_data=True,
    # To package with sdist only: add to MANIFEST.in, exclude below
    exclude_package_data={'myokit_beta': sdist_only_data},
    # To package with bdist only: include below
    package_data={'myokit_beta': bdist_only_data},

    # Supported Python versions
    python_requires='>=3.8',

    # List of dependencies
    install_requires=[
        'myokit>=1.34',
        'llvmlite>=0.37',
    ],

    ext_modules=[
        cvodes_sim,
    ],
)
