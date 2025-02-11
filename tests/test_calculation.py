"""
Tests the calculator's operations and the Calculation class, verifying basic arithmetic operations and functionality.
"""

from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

@pytest.mark.parametrize("operand1, operand2, operation, expected", [
    (Decimal('6'), Decimal('5'), add, Decimal('11')),
    (Decimal('10'), Decimal('5'), subtract, Decimal('5')),
    (Decimal('6'), Decimal('5'), multiply, Decimal('30')),
    (Decimal('6'), Decimal('2'), divide, Decimal('3')),
    (Decimal('9.5'), Decimal('0.5'), add, Decimal('10.0')),
    (Decimal('10.5'), Decimal('0.5'), subtract, Decimal('10.0')),
    (Decimal('10.5'), Decimal('2'), multiply, Decimal('21.0')),
    (Decimal('10'), Decimal('0.5'), divide, Decimal('20')),
])
def test_calculation_operations(operand1, operand2, operation, expected):
    """
    Test arithmetic operations with Decimal operands and ensure Calculation class returns expected results.
    """
    calc = Calculation(operand1, operand2, operation)
    assert calc.perform() == expected, f"Failed {operation.__name__} with {operand1} and {operand2}"

def test_calculation_repr():
    """
    Test the __repr__ method for accurate object representation.
    """
    calc = Calculation(Decimal('10'), Decimal('5'), add)
    expected_repr = "Calculation(10, 5, add)"
    assert repr(calc) == expected_repr, "Incorrect __repr__ output."

def test_divide_by_zero():
    """
    Ensure dividing by zero raises a ValueError.
    """
    calc = Calculation(Decimal('10'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.perform()