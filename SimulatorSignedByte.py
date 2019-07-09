from BoundedInteger import BoundedInteger


class SimulatorSignedByte(BoundedInteger):

    def __init__(self, value = 0):
        minimum = -(2**7)
        maximum = 2**7 - 1
        default = 0
        BoundedInteger.__init__(self, minimum, maximum, default)
        self.set(value)
