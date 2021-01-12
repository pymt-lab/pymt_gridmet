from __future__ import absolute_import

import pkg_resources
from gridmet_bmi import BmiGridmet as GridMet

GridMet.__name__ = "GridMet"
GridMet.METADATA = pkg_resources.resource_filename(__name__, "data/GridMet")

__all__ = [
    "GridMet",
]
