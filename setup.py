#!/usr/bin/env python

import os
from setuptools import setup

setup(name='mpas_analysis',
        version='0.0.0',
        description='Wrapper for xarray to interface with MPAS *.nc files',
        url='https://github.com/pwolfram/mpas_xarray/',
        maintainer='Los Alamos National Lab',
        maintainer_email='phillipwolfram@gmail.com',
        license='BSD',
        keywords='mpas analysis xarray',
        packages=['mpas_analysis'],
        install_requires=[open('requirements.txt').read().strip().split('\n')],
        long_description=(open('README.md').read() if os.path.exists('README.md') else ''),
        zip_safe=False)
