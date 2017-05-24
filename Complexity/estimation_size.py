from Complexity.complexity import complexity_estimate
import numpy as np
from scipy.special import lambertw
import math
from Complexity.executionHelpers import create_loggers_helper
import sys


def create_loggers():
    import logging
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.ERROR)
    logger = create_loggers_helper(logger)
    return logger


def estimation_size(file, fun, create_struct_fun, deadline, given_time):
    logger = create_loggers()
    try:
        (complexity_indexes, names_array, array_time, np_array_n) = \
            complexity_estimate(file, fun, create_struct_fun, deadline, True)
        if isinstance(complexity_indexes, list):
            complexity_indexes = complexity_indexes[0]
        if names_array[complexity_indexes] == names_array[0]:  # N
            constant = array_time[0] / np_array_n[0]
            return math.floor(given_time / constant)
        if names_array[complexity_indexes] == names_array[1]:  # N^2
            constant = array_time[0] / np_array_n[0] / np_array_n[0]
            return math.floor(np.sqrt(given_time / constant))
        elif names_array[complexity_indexes] == names_array[2]:  # N log N
            constant = array_time[0] / (np_array_n[0] * np.log(np_array_n[0]))
            tmp_value = given_time / constant
            return math.floor(tmp_value / lambertw(tmp_value))
    except Exception as e:
        print(e.args)
        logger.error("Exception was raised in estimation_size function")
        sys.exit(1)
