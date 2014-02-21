#!/usr/bin/env python

"""Python Demographics
===================

Generate gender and race estimates from name.  Based on 1990 Census
given name gender compilation [1] and the 2000 census surname race
compilation [2].

[1] http://www.census.gov/genealogy/www/data/1990surnames/names_files.html
[2] https://www.census.gov/genealogy/www/data/2000surnames/

"""

from setuptools import setup

setup(
    name='demographics',
    version='0.0.1',
    author='Adam DePrince',
    author_email='adeprince@nypublicradio.org',
    description='Estimate user\'s demographics from their name or email address.',
    url="",
    long_description=__doc__,
    py_modules=[
        'demographics/__init__',
        'demographics/data/__init__',
        'demographics/data/us/__init__',
        'demographics/data/us/race',
        'demographics/data/us/gender',
        ],
    packages=['demographics',],
    zip_safe=True,
    license='MIT',
    include_package_data=False,
    classifiers=[],
    scripts=[],
    install_requires=[
        ]
    )
