import unittest
from SimulatorSignedWord import SimulatorSignedWord
from SimulatorExceptions import ValueOutOfRangeException


class SimulatorSignedWordTest(unittest.TestCase):

    def test_constructor(self):

        # Test default value

        simulator_type = SimulatorSignedWord()
        self.assertEqual(simulator_type.get(), simulator_type.default)

        # Test initial value

        simulator_type = SimulatorSignedWord(simulator_type.minimum)
        self.assertEqual(simulator_type.get(), simulator_type.minimum)

        simulator_type = SimulatorSignedWord(simulator_type.maximum)
        self.assertEqual(simulator_type.get(), simulator_type.maximum)

        # Test invalid initial value

        with self.assertRaises(ValueOutOfRangeException):
            simulator_type = SimulatorSignedWord(simulator_type.minimum - 1)

        with self.assertRaises(ValueOutOfRangeException):
            simulator_type = SimulatorSignedWord(simulator_type.maximum + 1)


if __name__ == '__main__':
    unittest.main()
