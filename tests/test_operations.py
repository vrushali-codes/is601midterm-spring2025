"""
This module contains tests for various calculator operations, specifically testing the Calculation class.
"""
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import divide


def test_operation(a, b, operation, expected):# pylint: disable=invalid-name
    '''Testing various operations'''
    calculation = Calculation.create(a, b, operation)
    assert calculation.perform() == expected, f"{operation.__name__} operation failed"

def test_divide_by_zero():
    '''Testing the divide by zero exception'''
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculation = Calculation(Decimal('10'), Decimal('0'), divide)
        calculation.perform()