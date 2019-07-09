from BoundedInteger import BoundedInteger


class SimulatorUnsignedHalfword(BoundedInteger):

    def __init__(self, value = 0):
        minimum = 0
        maximum = 2**16 - 1
        default = 0
        BoundedInteger.__init__(self, minimum, maximum, default)
        self.set(value)
