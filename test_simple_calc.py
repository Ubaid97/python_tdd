from simple_calc import SimpleCalc

import unittest
import pytest

# class to write tests
class CalcTest(unittest.TestCase):
# unittest.TestCase is a framework with unittest as Parent class

# create instance of class to be tested
    calc = SimpleCalc()

    # use 'test' in function name so python interpreter understands that this is a test function
    def test_add(self):
        self.assertEqual(self.calc.add(2, 4), 6) # Boolean: is add(2, 4) == 6
        # Tests to see whether passing in (2, 4) in the add function of SimpleClass returns 6
        # 2 + 4 = 6

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4, 2), 2) # Boolean: is subtract(4, 2) == 2
        # Tests to see whether passing in (4, 2) in the add function of SimpleClass returns 2
        # 4 - 2 = 2

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 2), 4) # Boolean: is multiply(2, 2) == 4
        # Tests to see whether passing in (2, 2) in the add function of SimpleClass returns 4
        # 2 * 2 = 4

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 3), 2) # Boolean: is divide(6, 3) == 2
        # Tests to see whether passing in (2, 4) in the add function of SimpleClass returns 6
        # 6 / 3 = 2