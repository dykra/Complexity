import importlib
import time


def create_loggers_helper(logger):
    import logging
    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # add formatter to ch
    ch.setFormatter(formatter)
    # add ch to logger
    logger.addHandler(ch)
    return logger


def create_loggers():
    import logging
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.ERROR)
    logger = create_loggers_helper(logger)
    return logger


def entry_fun(f):
    def new_f(*args, **kwargs):
        logger = create_loggers()
        logger.debug('I am in function ' + f.__name__)
        try:
            f(*args, **kwargs)
        except Exception as e:
            logger.warning('Exception was raised in ' + f.__name__)
            logger.warning(e.args)
            raise
        logger.debug(f.__name__ + 'was executed correctly.')
    return new_f


@entry_fun
def exec_fun_without_output(file_name, fun, args):
    module = importlib.import_module(file_name)
    function = getattr(module, fun)
    function(args)


@entry_fun
def exec_fun_with_time(file, struct_create_fun, fun, N):
    module = importlib.import_module(file)  # file
    function = getattr(module, struct_create_fun)
    structure = function(N)
    time1 = time.time()
    exec_fun_without_output(file, fun, structure)
    time2 = time.time()
    result = time2 - time1
    return result

