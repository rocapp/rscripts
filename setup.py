#!/usr/bin/env python

from setuptools import setup, find_packages
import os


setup(name='rscripts',
      version='0.1a4',
      description='quick scripts for many different uses',
      author='Robbie Capps',
      author_email='rocapp@gmail.com',
      url='https://github.com/rocapp/rscripts',
      package_dir={'rscripts': 'rscripts'},
      packages=find_packages(),
      install_requires=['matplotlib','numpy']
     )
