# Test Driven Development
- TDD helps minimise errors in a product
- python has several modules we can use to test code:
    - pytest
    - unittest

**Steps**
- Create a file to write tests
- Write failing tests
- Write code to make those tests pass
- Write new failing tests...

**Naming conventions for files**
- simple_calc
- test_simple_calc

### Calculator example
- given the aim of creating a function that takes in two numbers and adds them together, we would first create  test class by importing pytest, unittest, and the class containing the function to be tested:
```python
from simple_calc import SimpleCalc
import unittest
import pytest
```
- then create an instance of the class to bes tested within the test class
```python
class CalcTest(unittest.TestCase):
# unittest.TestCase is a framework with unittest as Parent class
    # create instance of class to be tested
    calc = SimpleCalc()
```
- create a test function for a particular function:
```python
# use 'test' in function name so python interpreter understands that this is a test function
    def test_add(self):
        self.assertEqual(self.calc.add(2, 4), 6) # Boolean: is add(2, 4) == 6
        # Tests to see whether passing in (2, 4) in the add function of SimpleClass returns 6
        # 2 + 4 = 6
```
- the function being tested by the above test case is:
```python
    def add(self, num1, num2):
        return num1 + num2
```
- you can run the tests by entering ```pytest -v``` in the terminal
