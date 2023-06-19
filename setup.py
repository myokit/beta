#!/usr/bin/env python3
import platform

from setuptools import find_namespace_packages, setup, Extension


# Load text for description and license
with open('README.md') as f:
    readme = f.read()


# Platform differences
system = platform.system()
if system == 'Windows':
    sundials_inc = ['src/myokit_beta/_win/sundials-vs/inc']
    sundials_lib = ['src/myokit_beta/_win/sundials-vs/lib']
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


# Package data (will be refined below)
pkg_exclude = []
if system != 'Windows':
    pkg_exclude.extend(['myokit_beta._win', 'myokit_beta._win.*'])


# CVODES Simulation
sim_libraries = ['sundials_cvodes', 'sundials_nvecserial']
if system != 'Windows':
    sim_libraries.append('m')
cvodes_sim = Extension(
    'myokit_beta._sim._cvodessim_ext',
    sources=['src/myokit_beta/_sim/_cvodessim.c'],
    libraries=sim_libraries,
    library_dirs=sundials_lib,
    include_dirs=sundials_inc,
    #runtime_library_dirs=runtime,
)

print(find_namespace_packages(where='src'))

# Go!
setup(
    name='myokit_beta',

    # Version
    version='0.0.7',

    # Description
    description='Trying out distribution of wheels etc and llvm',
    long_description=readme,
    long_description_content_type='text/markdown',

    # Packages to include
    packages=find_namespace_packages('src', exclude=pkg_exclude),
    package_dir={'': 'src'},
    package_data={
        '': ['*'],
    },

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
