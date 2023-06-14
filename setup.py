#!/usr/bin/env python3
import platform

from setuptools import find_packages, setup, Extension


# Load text for description and license
with open('README.md') as f:
    readme = f.read()


# Platform differences
system = platform.system()
if system == 'Darwin':
    sundials_lib = ['/opt/homebrew/lib']
    sundials_inc = ['/opt/homebrew/include']
elif system == 'Windows':
    sundials_lib = ['./lib/sundials-win-vs/lib']
    sundials_inc = ['./lib/sundials-win-vs/include']
else:
    sundials_lib = ['/usr/local/lib']
    sundials_inc = ['/usr/local/include']



# CVODES Simulation
sim_libraries = ['sundials_cvodes', 'sundials_nvecserial']
if platform.system() != 'Windows':
    sim_libraries.append('m')
cvodes_sim = Extension(
    'myokit_beta._sim.sim1',
    sources=['src/sim1.c'],
    libraries=sim_libraries,
    library_dirs=sundials_lib,
    include_dirs=sundials_inc,
    #runtime_library_dirs=runtime,
)



# Go!
setup(
    name='myokit_beta',

    # Version
    version='0.0.5',

    # Description
    description='Trying out distribution of wheels etc and llvm',
    long_description=readme,
    long_description_content_type='text/markdown',

    # Packages to include
    packages=find_packages(include=('myokit_beta', 'myokit_beta.*')),

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
