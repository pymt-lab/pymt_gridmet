============
pymt_gridmet
============


.. image:: https://img.shields.io/badge/CSDMS-Basic%20Model%20Interface-green.svg
        :target: https://bmi.readthedocs.io/
        :alt: Basic Model Interface

.. image:: https://img.shields.io/badge/recipe-pymt_gridmet-green.svg
        :target: https://anaconda.org/conda-forge/pymt_gridmet

.. image:: https://img.shields.io/travis/rmcd-mscb/pymt_gridmet.svg
        :target: https://travis-ci.org/rmcd-mscb/pymt_gridmet

.. image:: https://readthedocs.org/projects/pymt-gridmet/badge/?version=latest
        :target: https://pymt-gridmet.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
        :target: https://github.com/csdms/pymt
        :alt: Code style: black


PyMT component for accessing gridMET data


* Free software: MIT License
* Documentation: https://pymt-gridmet.readthedocs.io.




========= ===================================
Component PyMT
========= ===================================

GridMet   `from pymt.models import GridMet`
========= ===================================

---------------
Installing pymt
---------------

Installing `pymt` from the `conda-forge` channel can be achieved by adding
`conda-forge` to your channels with:

.. code::

  conda config --add channels conda-forge

*Note*: Before installing `pymt`, you may want to create a separate environment
into which to install it. This can be done with,

.. code::

  conda create -n pymt python=3
  conda activate pymt

Once the `conda-forge` channel has been enabled, `pymt` can be installed with:

.. code::

  conda install pymt

It is possible to list all of the versions of `pymt` available on your platform with:

.. code::

  conda search pymt --channel conda-forge

-----------------------
Installing pymt_gridmet
-----------------------



To install `pymt_gridmet`,

.. code::

  conda install pymt_gridmet
