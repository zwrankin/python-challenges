#!/usr/bin/env python

from distutils.core import setup
# from glob import glob

from setuptools import find_packages

setup(name='pychallenge',
      version='0.1',
      description='Pythonic Challenges',
      author='Zane Rankin',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      # py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
      )
