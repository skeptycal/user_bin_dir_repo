#!/usr/bin/env python3

# https://raw.githubusercontent.com/xvxvxvxvxv/python_vs_numpy_arrays_iteration/master/test_python_numpy_arrays.py

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
    start = timer()
    for _ in np.nditer(arr):
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
