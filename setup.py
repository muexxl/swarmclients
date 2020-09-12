# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='swarmclients',
    version='0.1.0',
    description='Swarmclients is a package for managing multiple clients',
    long_description=readme,
    author='Stephan Muekusch',
    author_email='stephan@1drone.de',
    url='',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

