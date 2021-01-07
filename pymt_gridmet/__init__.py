#! /usr/bin/env python
import pkg_resources

__version__ = pkg_resources.get_distribution("pymt_gridmet").version


from .bmi import GridMet

__all__ = [
    "GridMet",
]
