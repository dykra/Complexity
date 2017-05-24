# -*- coding: utf-8 -*-

import numpy as np
import signal
import sys
from Complexity.executionHelpers import exec_fun_with_time, create_loggers_helper, exec_fun_without_output
from Complexity.exceptions import TimeOutException
import importlib
import time


def create_loggers():
    import logging
    logger = create_loggers_helper(logging.getLogger(__name__))
    logger.setLevel(logging.ERROR)
    return logger


def complexity_estimate(structure, fun, create_struct_fun, time, given_array):
    logger = create_loggers()
    logger.debug("I am in complexity_estimate.")
    np_array__n = np.array(list(range(1000, 100000000, 1000)))  # tablica z wartościami N
    array_time = pack_create_array(time, np_array__n, structure, fun, create_struct_fun)
    np_array_time = np.array(array_time)
    names_array = ["n", "n * log(n)", "n^2"]
    if np_array_time.size < np_array__n.size:
        np_array__n = np.delete(np_array__n, list(range(np_array_time.size, np_array__n.size)))
    np_tmp_array = np.array([np.var(np.log(np_array_time / np_array__n)),
                            np.var(np.var(np.log(np_array_time / (np_array__n * np.log(np_array__n))))),
                            np.var(np.var(np.log(np_array_time / np_array__n ** 2)))]
                            )
    logger.info("complexity_ estimate finished correctly.")
    if not given_array:
        if np_tmp_array.min() == 0:
            return [i for (i, x) in enumerate(np_tmp_array) if x == 0], names_array
        return np_tmp_array.argmin(), names_array  # gives the index corresponding to the minimum
    if np_tmp_array.min() == 0:
        return [i for (i, x) in enumerate(np_tmp_array) if x == 0], names_array, array_time, np_array__n
    return np_tmp_array.argmin(), names_array, array_time, np_array__n  # gives the index corresponding to the minimum


def dead_line(timeout, *args, **kwargs):
    print("Timeout is " + "%s" % timeout)

    def decorate(f):
        logger = create_loggers()
        logger.info("I am decorating " + f.__name__)

        def handler(signum, frame):
            logger.warning("TimeOut exception is going to be raised in " + f.__name__)
            raise TimeOutException("Deadline for creating table.")

        def new_f(*args, **kwargs):
            signal.signal(signal.SIGALRM, handler)
            signal.alarm(timeout)
            return f(*args, **kwargs)
        new_f.func_name = f.__name__
        return new_f
    return decorate


def give_complexity(file, fun, create_struct_fun, time):
    (minimum, names_array) = complexity_estimate(file, fun, create_struct_fun, time, False)
    if isinstance(minimum, list):
        logger = create_loggers()
        logger.info("Few results are highly possible")
        return [names_array[i] for i in minimum]
    return names_array[minimum]


def pack_create_array(deadline, np_array__n, file, fun, create_struct_fun):
    @dead_line(deadline)
    def create_array_with_times(np_array__n, file, fun, create_struct_fun):
        logger = create_loggers()
        logger.info("I am in create_array")
        np_array_time = []
        for i in range(np_array__n.size):
            try:
                # time_execution = exec_fun_with_time(file, create_struct_fun, fun, np_array__n[i])
                module = importlib.import_module(file)
                function = getattr(module, create_struct_fun)
                structure = function(np_array__n[i])
                time1 = time.time()
                exec_fun_without_output(file, fun, structure)
                time2 = time.time()
                time_execution = (time2 - time1) * 1000000
                np_array_time.append(time_execution)
            except TimeOutException:
                logger.warning("Creating time array was interrupted.")
                break
            except Exception as e:
                print(e.args)
                logger.error("Exception was raised in create_array")
                sys.exit(1)
        return np_array_time
    return create_array_with_times(np_array__n, file, fun, create_struct_fun)
