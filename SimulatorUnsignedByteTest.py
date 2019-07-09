import unittest
from SimulatorUnsignedByte import SimulatorUnsignedByte
from SimulatorExceptions import ValueOutOfRangeException


class SimulatorUnsignedByteTest(unittest.TestCase):

    def test_constructor(self):

        minimum = 0
        maximum = 2**8

        # Test default value

        simulator_type = SimulatorUnsignedByte()
        self.assertEqual(simulator_type.get(), simulator_type.default)

        # Test initial value

        simulator_type = SimulatorUnsignedByte(simulator_type.minimum)
        self.assertEqual(simulator_type.get(), simulator_type.minimum)

        simulator_type = SimulatorUnsignedByte(simulator_type.maximum)
        self.assertEqual(simulator_type.get(), simulator_type.maximum)

        # Test invalid initial value

        with self.assertRaises(ValueOutOfRangeException):
            simulator_type = SimulatorUnsignedByte(simulator_type.minimum - 1)

        with self.assertRaises(ValueOutOfRangeException):
            simulator_type = SimulatorUnsignedByte(simulator_type.maximum + 1)


if __name__ == '__main__':
    unittest.main()
