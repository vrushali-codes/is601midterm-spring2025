"""
Test module for calculator operations and Calculation class.
"""

from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, divide

# pylint: disable=invalid-name
def test_calculation_operations(a, b, operation, expected):
    """Test arithmetic operations with Calculation class."""
    calc = Calculation(a, b, operation)
    assert calc.perform() == expected, f"Failed {operation.__name__} with {a} and {b}"

def test_calculation_repr():
    """Test repr method of Calculation class."""
    calc = Calculation(Decimal('10'), Decimal('5'), add)
    expected_repr = "Calculation(10, 5, add)"
    assert repr(calc) == expected_repr, "Incorrect repr output."

def test_divide_by_zero():
    """Test division by zero raises ValueError."""
    calc = Calculation(Decimal('10'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.perform()