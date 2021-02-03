gridMET data component
======================

The gridMET data component, *pymt_gridmet*,
is a `Python Modeling Toolkit`_ (*pymt*) library
for fetching and caching daily `gridMET`_ meteorological data.
Variables include:

* maximum temperature
* minimum temperature
* precipitation accumulation

The *pymt_gridmet* component provides `BMI`_-mediated access to gridMET data as a service,
allowing it to be coupled with other components that expose a BMI.


Installation
------------

*pymt*, and components that run within it,
are distributed through `Anaconda`_ and the `conda`_ package manager.
Instructions for `installing`_ Anaconda can be found on their website.
In particular,
*pymt* components are available through the `conda-forge`_ organization.

Install the `pymt` and `pymt_gridmet` packages in a new environment with:

.. code::

  $ conda create -n pymt -c conda-forge python=3 pymt pymt_gridmet
  $ conda activate pymt

*conda* automatically resolves and installs any required dependencies.


Use
---

The *pymt_gridmet* data component is designed to access daily gridMET data,
with the user providing the start and end dates of the desired data record.
The dates can be provided through a configuration file
or specified through parameters.

With a configuration file
.........................

The *pymt_gridmet* configuration file is a `YAML`_ file
containing two keys, `_start_date` and `_end_date`.
An example is :download:`gridmet.yaml`:

.. include:: gridmet.yaml
   :literal:

:download:`Download <gridmet.yaml>` this file
for use in the following example.

.. include:: pymt_gridmet_config_file_ex.rst


With parameters
...............

The start and end dates can also be passed directly to *pymt_gridmet* as parameters.

.. include:: pymt_gridmet_parameters_ex.rst


Indices and tables
==================
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


.. Links:

.. _Python Modeling Toolkit: https://pymt.readthedocs.io
.. _gridmet: http://www.climatologylab.org/gridmet.html
.. _BMI: https://bmi.readthedocs.io
.. _Anaconda: https://www.anaconda.com/products/individual
.. _conda: https://docs.conda.io/en/latest/
.. _installing: https://docs.anaconda.com/anaconda/install/
.. _conda-forge: https://conda-forge.org/
.. _YAML: https://en.wikipedia.org/wiki/YAML
