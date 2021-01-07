#! /usr/bin/env python
import os
import sys

from setuptools import Extension, find_packages, setup

entry_points = {
    "pymt.plugins": [
        "GridMet=pymt_gridmet.bmi:GridMet",
    ]
}


def read(filename):
    with open(filename, "r", encoding="utf-8") as fp:
        return fp.read()


long_description = u"\n\n".join(
    [read("README.rst"), read("CREDITS.rst"), read("CHANGES.rst")]
)


setup(
    name="pymt_gridmet",
    author="Rich McDonald",
    author_email="rmcd@usgs.gov",
    description="PyMT plugin for pymt_gridmet",
    long_description=long_description,
    version="0.1",
    url="https://github.com/rmcd-mscb/pymt_gridmet",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
    ],
    keywords=["bmi", "pymt"],
    install_requires=open("requirements.txt", "r").read().splitlines(),
    packages=find_packages(),
    entry_points=entry_points,
    include_package_data=True,
)
