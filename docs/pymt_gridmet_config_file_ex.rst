Start by importing the GridMet class from ``pymt``.

.. code:: ipython3

    from pymt.models import GridMet

Create an instance of the GridMet class and initialize it with our
configuration file.

.. code:: ipython3

    m = GridMet()
    m.initialize("gridmet.yaml")


.. parsed-literal::

    gridmet.yaml
    ...
    


Note that the start and end dates have been read from the configuration
file into the component as parameters.

.. code:: ipython3

    for param in m.parameters:
        print(param)


.. parsed-literal::

    ('start_date', '2020-01-01')
    ('end_date', '2020-01-07')


What variables can be accessed from this data component?

.. code:: ipython3

    for var in m.output_var_names:
        print(var)


.. parsed-literal::

    daily_maximum_temperature
    daily_minimum_temperature
    precipitation_amount


Get the maximum temperature values for the first day.

.. code:: ipython3

    Tmax = m.var["daily_maximum_temperature"]
    Tmax_values = Tmax.data

What is the maximum maximum temperature? (Note that the data include NaN
values, which we can ignore with ``numpy.nanmax``.)

.. code:: ipython3

    import numpy
    
    numpy.nanmax(Tmax_values)




.. parsed-literal::

    305.70001



But what are the units of this temperature value?

.. code:: ipython3

    Tmax.units




.. parsed-literal::

    'K'



Finish by finalizing the component. This cleans up resource, including
deleting downloaded data files.

.. code:: ipython3

    m.finalize()
