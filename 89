import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    assert add(3, 2) == 5

def test_subtract():
    assert subtract(5, 2) == 3

def test_multiply():
    assert multiply(4, 3) == 12

def test_divide():
    assert divide(10, 2) == 5
    with pytest.raises(ValueError):
        divide(5, 0)

# Run with:
# pytest test_calculator.py

@pytest.mark.parametrize("a, b, expected", [(3, 2, 5), (0, 5, 5), (-3, 3, 0)])
def test_add_param(a, b, expected):
    assert add(a, b) == expected