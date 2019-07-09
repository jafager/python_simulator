from BoundedInteger import BoundedInteger


class SimulatorSignedHalfword(BoundedInteger):

    def __init__(self, value = 0):
        minimum = -(2**15)
        maximum = 2**15 - 1
        default = 0
        BoundedInteger.__init__(self, minimum, maximum, default)
        self.set(value)
