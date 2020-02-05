# CURTOSY OF https://www.tutorialspoint.com/pytest/pytest_conftest_py.htm
import pytest

"""
@pytest.fixture
def input_value():
   input = 39
   return input

def test_divisible_by_3(input_value):
   assert input_value % 3 == 0

def test_divisible_by_6(input_value):
   assert input_value % 6 == 0
"""

def test_add():
   x = 3 + 4
   assert x == 5