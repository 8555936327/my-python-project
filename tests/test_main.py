# tests/test_main.py
from ..main import add, subtract, multiply, divide
import pytest
from main import some_function

def test_some_function():
    assert some_function(2, 3) == 5  # example test
