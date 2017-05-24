import numpy as np
from Complexity.complexity import complexity_estimate
import sys
from Complexity.executionHelpers import create_loggers_helper


def create_loggers():
    import logging
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.ERROR)
    logger = create_loggers_helper(logger)
    return logger


def estimation_time(file, fun, create_struct_fun, deadline, n):
    logger = create_loggers()
    logger.debug("I am in estimation_time function.")
    (complexity_indexes, names_array, array_time, np_array_n) = complexity_estimate(file, fun, create_struct_fun, deadline, True)
    try:
        if isinstance(complexity_indexes, list):
            complexity_indexes = complexity_indexes[0]
            logger.debug('Variable with results turned out to be a list.')
        if names_array[complexity_indexes] == names_array[0]:  # N
            constant = array_time[0] / np_array_n[0]
            return constant * n
        if names_array[complexity_indexes] == names_array[1]:  # N^2
            constant = array_time[0] / np_array_n[0] / np_array_n[0]
            return constant * n * n
        elif names_array[complexity_indexes] == names_array[2]:  # N log N
            constant = array_time[0] / (np_array_n[0] * np.log(np_array_n[0]))
            return constant * n * np.log(n)
    except Exception as e:
        print(e.args)
        logger.error("Exception was raised in estimation_time function")
        sys.exit(1)

