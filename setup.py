#!/usr/bin/env python

from distutils.core import setup

setup(name='rscripts',
      version='0.023',
      description='quick scripts',
      author='Robbie Capps',
      author_email='rocapp@gmail.com',
      url='https://robcapps.com',
      packages=['rscripts'],
      package_dir={'rscripts': 'src/rscripts'}
     )