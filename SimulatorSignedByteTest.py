import unittest
from SimulatorSignedByte import SimulatorSignedByte
from SimulatorExceptions import ValueOutOfRangeException


class SimulatorSignedByteTest(unittest.TestCase):

    def test_constructor(self):

        # Test default value

        simulator_type = SimulatorSignedByte()
        self.assertEqual(simulator_type.get(), simulator_type.default)

        # Test initial value

        simulator_type = SimulatorSignedByte(simulator_type.minimum)
        self.assertEqual(simulator_type.get(), simulator_type.minimum)

        simulator_type = SimulatorSignedByte(simulator_type.maximum)
        self.assertEqual(simulator_type.get(), simulator_type.maximum)

        # Test invalid initial value

        with self.assertRaises(ValueOutOfRangeException):
            simulator_type = SimulatorSignedByte(simulator_type.minimum - 1)

        with self.assertRaises(ValueOutOfRangeException):
            simulator_type = SimulatorSignedByte(simulator_type.maximum + 1)


if __name__ == '__main__':
    unittest.main()
