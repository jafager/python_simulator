class SimulatorException(Exception):
    pass


class ValueOutOfRangeException(SimulatorException):

    def __init__(self, value):
        self.value = value
