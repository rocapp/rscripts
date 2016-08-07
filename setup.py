#!/usr/bin/env python

from setuptools import setup, find_packages
import os


setup(name='rscripts',
      version='0.023',
      description='quick scripts for many different uses',
      author='Robbie Capps',
      author_email='rocapp@gmail.com',
      url='https://robcapps.com',
      packages=map(lambda path: os.path.join('src', path), find_packages(where='src'))
     )
