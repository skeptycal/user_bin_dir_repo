#!/usr/bin/env python3
""" array — Efficient arrays of numeric values
    https://docs.python.org/3.6/library/array.html

    Type code   C Type              Python Type         Minimum size in bytes           Notes
    ----------------------------------------------------------------------------------------
        'b'     signed char             int                     1
        'B'     unsigned char           int                     1
    ----------------------------------------------------------------------------------------
        'u'     Py_UNICODE Unicode      character               2                       (1)
        'h'     signed short            int                     2
        'H'     unsigned short          int                     2
        'i'     signed int              int                     2
        'I'     unsigned int            int                     2
    ----------------------------------------------------------------------------------------
        'l'     signed long             int                     4
        'L'     unsigned long           int                     4
        'f'     float                   float                   4
    ----------------------------------------------------------------------------------------
        'q'     signed long             long int                8                       (2)
        'Q'     unsigned long           long int                8                       (2)
        'd'     double                  float                   8

    Notes:

    (1) The 'u' type code corresponds to Python’s obsolete unicode character (Py_UNICODE which is wchar_t). Depending on the platform, it can be 16 bits or 32 bits.

    'u' will be removed together with the rest of the Py_UNICODE API.

    Deprecated since version 3.3, will be removed in version 4.0.

    (2) The 'q' and 'Q' type codes are available only if the platform C compiler used to build Python supports C long long, or, on Windows, __int64.

    New in version 3.3.

    The actual representation of values is determined by the machine architecture (strictly speaking, by the C implementation). The actual size can be accessed through the itemsize attribute.

    """

from array import array
from collections import defaultdict
from timeit import default_timer as timer

import numpy as np


def export_picture(measurements, size_of_arrays):

    import matplotlib.pyplot as plt
    import pandas as pd

    df = pd.DataFrame(measurements)
    df['length'] = size_of_arrays

    df.set_index('length', inplace=True, drop=True)
    ax = df.plot(title="Python array vs Numpy array iteration speed")

    ax.set_ylabel("seconds")
    ax.set_xlabel(f"length of array")

    ax.get_xaxis().get_major_formatter().set_useOffset(False)
    ax.get_xaxis().get_major_formatter().set_scientific(False)
    ax.get_yaxis().get_major_formatter().set_useOffset(False)
    ax.get_yaxis().get_major_formatter().set_scientific(False)

    plt.savefig('measurements.png', dpi=300)


def iterate_over_array(arr):
    start = timer()
    for _ in arr:
        pass
    return timer() - start


def iterate_numpy_nditer(arr):
    _npiter = np.nditer(arr)  # eliminate function call within loop ...
    start = timer()
    for _ in _npiter:
        pass
    return timer() - start


def make_arrays(list_of_numbers):
    measurements = defaultdict(list)
    for number in list_of_numbers:
        np_array = np.arange(float(number))
        python_array = array('d', np_array)

        measurements[f'nditer(numpy)'].append(iterate_numpy_nditer(np_array))
        measurements[f'nditer(memoryview(numpy))'].append(
            iterate_numpy_nditer(memoryview(np_array))
        )
        measurements[f'numpy'].append(iterate_over_array(np_array))
        measurements[f'memoryview(numpy)'].append(
            iterate_over_array(memoryview(np_array))
        )
        measurements[f'memoryview(python)'].append(
            iterate_over_array(memoryview(python_array)))
        measurements[f'python'].append(iterate_over_array(python_array))
    return measurements


def check_same_values(values):
    # Double check that we get the same values in both arrays.
    for value in values:
        np_array = np.arange(float(value))
        python_array = array('d', np_array)

        _np = [x for x in np_array]
        pp = [x for x in python_array]

        assert _np == pp


list_of_numbers = [
    50,
    100,
    500,
    1000,
    5000,
    10_000,
    50_000,
    100_000,
    500_000,
    1_000_000,
]
check_same_values(list_of_numbers)
measurements = make_arrays(list_of_numbers)
#export_picture(measurements, list_of_numbers)
