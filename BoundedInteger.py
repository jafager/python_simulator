from SimulatorExceptions import ValueOutOfRangeException


class BoundedInteger:

    def __init__(self, minimum, maximum, default):
        assert (minimum <= maximum)
        assert (default >= minimum)
        assert (default <= maximum)
        self.minimum = minimum
        self.maximum = maximum
        self.default = default
        self.value = default

    def get(self):
        value = self.value
        assert (value >= self.minimum)
        assert (value <= self.maximum)
        return value

    def set(self, value):
        if ((value >= self.minimum) and (value <= self.maximum)):
            self.value = value
        else:
            raise ValueOutOfRangeException(value)
