#!/usr/bin/env python

from setuptools import setup


with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(name='tap-sendgrid',
      version='0.1.0',
      description='Singer.io tap for extracting data from the SendGrid API',
      author='Jamie MacLeod',
      url='http://singer.io',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['tap_sendgrid'],
      install_requires=requirements,
      entry_points='''
          [console_scripts]
          tap-sendgrid=tap_sendgrid.tap:cli
      ''',
      packages=['tap_sendgrid'],
      include_package_data=True
)