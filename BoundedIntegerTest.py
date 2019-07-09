import unittest
from BoundedInteger import BoundedInteger
from SimulatorExceptions import ValueOutOfRangeException


class BoundedIntegerTest(unittest.TestCase):

    def test_constructor(self):

        # Test default value

        bounded_integer = BoundedInteger(0, 10, 0)
        self.assertEqual(bounded_integer.get(), 0)

        bounded_integer = BoundedInteger(-10, 10, 5)
        self.assertEqual(bounded_integer.get(), 5)

        # Test minimum > maximum

        with self.assertRaises(AssertionError):
            bounded_integer = BoundedInteger(10, 0, 0)

        with self.assertRaises(AssertionError):
            bounded_integer = BoundedInteger(10, -10, 5)

        # Test default value not between minimum/maximum

        with self.assertRaises(AssertionError):
            bounded_integer = BoundedInteger(0, 10, 11)

        with self.assertRaises(AssertionError):
            bounded_integer = BoundedInteger(-10, 10, -15)

    def test_getset(self):

        # Test valid values

        bounded_integer = BoundedInteger(0, 10, 0)

        bounded_integer.set(1)
        self.assertEqual(bounded_integer.get(), 1)

        bounded_integer.set(10)
        self.assertEqual(bounded_integer.get(), 10)

        bounded_integer = BoundedInteger(-10, 10, 0)

        bounded_integer.set(-10)
        self.assertEqual(bounded_integer.get(), -10)

        bounded_integer.set(10)
        self.assertEqual(bounded_integer.get(), 10)

        # Test invalid values

        bounded_integer = BoundedInteger(0, 10, 0)

        with self.assertRaises(ValueOutOfRangeException):
            bounded_integer.set(-1)

        with self.assertRaises(ValueOutOfRangeException):
            bounded_integer.set(11)

        bounded_integer = BoundedInteger(-10, 10, 0)

        with self.assertRaises(ValueOutOfRangeException):
            bounded_integer.set(-11)

        with self.assertRaises(ValueOutOfRangeException):
            bounded_integer.set(11)


if __name__ == '__main__':
    unittest.main()
