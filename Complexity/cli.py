# -*- coding: utf-8 -*-

import click
import sys
from Complexity.complexity import give_complexity
from Complexity.executionHelpers import exec_fun_without_output, create_loggers_helper
from Complexity.exceptions import NoMandatoryArgumentsExc, AmountArgumentExc, MinusArgumentExc, TooBigNumberExc
from Complexity.estimation_size import estimation_size
from Complexity.estimation_time import estimation_time


@click.command()
@click.option('--complexity', default=False)
@click.option('--file', default=False)
@click.option('--fun', default=False, help='Function or class to execute')
@click.option('--clean',  default=False)
@click.option('--deadline', default=30, type=int)
@click.option('--estimate', default=('0', '0', 0), nargs=3, type=(str, str, int))
def main(file, fun, clean, complexity, deadline, estimate):
    """Console script for Complexity"""

    import logging.config
    logger = create_loggers_helper(logging.getLogger(__name__))
    logger.setLevel(logging.DEBUG)
    logger.info('I have started the execution.')
    click.echo("Complexity estimator")

    try:
        if file.endswith('.py'):
            file = file[:-3]
    except Exception as e:
        print("You have to specify file name.")
        logger.error('Exception was raised')
        click.echo(e.args)
        sys.exit(1)

    try:
        if not fun:
            raise NoMandatoryArgumentsExc("Fun has to be specified.")
    except NoMandatoryArgumentsExc as e:
        logger.error('Exception NoMandatoryArgumentsError was raised')
        print(e.msg)
        sys.exit(1)
    try:
        if not complexity and estimate == ():
            raise AmountArgumentExc("Nothing was chosen.")
        if complexity:
            is_complexity = True
        else:
            is_complexity = False

        if sum([estimate != ('0', '0', 0), is_complexity]) > 1:
            raise AmountArgumentExc("You have chosen too much.")
    except AmountArgumentExc as e:
        logger.error('Exception was raised')
        print(e.msg, e.args)
        sys.exit(1)

    try:
        if estimate != () and estimate[2] < 0:
            raise MinusArgumentExc("Estimate argument lower than 0.")
        if deadline < 0:
            raise MinusArgumentExc("Time for execution lower than 0.")
        if estimate != () and estimate[2] < 0:
            raise MinusArgumentExc("Time to estimate size of the problem was lower than 0.")
    except MinusArgumentExc as e:
        logger.error('Exception was raised')
        print(e.args)
        sys.exit(1)
    try:
        if deadline > 1000000:
            raise TooBigNumberExc("Time for execution is too long.")
    except TooBigNumberExc as er:
        logger.error('Exception was raised')
        print(er.args)
        sys.exit(1)
    try:
        if complexity:
            print(give_complexity(file, fun, complexity, deadline))
        if estimate != ('0', '0', 0) and estimate[1] == 'size':
            print(estimation_size(file, fun, estimate[0], deadline, estimate[2]))
        elif estimate != ('0', '0', 0):
            print(estimation_time(file, fun, estimate[0], deadline, estimate[2]))
        if clean:
            exec_fun_without_output(file, clean, "I want to clean")
    except Exception as e:
        logger.error('Exception was raised')
        click.echo(e.args)
        sys.exit(1)

if __name__ == "__main__":
    main()
