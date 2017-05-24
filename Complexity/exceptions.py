class Error(Exception):
    pass  # nothing is happening


class TooBigNumberExc(Error):
    def __init__(self, arg):
        self.args = arg


class MinusArgumentExc(Error):
    def __init__(self, arg):
        self.args = arg


class AmountArgumentExc(Error):
    def __init__(self, msg):
        self.args = "You have to choose one option."
        self.msg = msg


class NoMandatoryArgumentsExc(Error):
    def __init__(self, msg):
        self.msg = msg


class TimeOutException(Error):
    def __init__(self, arg):
        self.args = arg
