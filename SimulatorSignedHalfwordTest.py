import unittest
from SimulatorSignedHalfword import SimulatorSignedHalfword
from SimulatorExceptions import ValueOutOfRangeException


class SimulatorSignedHalfwordTest(unittest.TestCase):

    def test_constructor(self):

        # Test default value

        simulator_type = SimulatorSignedHalfword()
        self.assertEqual(simulator_type.get(), simulator_type.default)

        # Test initial value

        simulator_type = SimulatorSignedHalfword(simulator_type.minimum)
        self.assertEqual(simulator_type.get(), simulator_type.minimum)

        simulator_type = SimulatorSignedHalfword(simulator_type.maximum)
        self.assertEqual(simulator_type.get(), simulator_type.maximum)

        # Test invalid initial value

        with self.assertRaises(ValueOutOfRangeException):
            simulator_type = SimulatorSignedHalfword(simulator_type.minimum - 1)

        with self.assertRaises(ValueOutOfRangeException):
            simulator_type = SimulatorSignedHalfword(simulator_type.maximum + 1)


if __name__ == '__main__':
    unittest.main()
