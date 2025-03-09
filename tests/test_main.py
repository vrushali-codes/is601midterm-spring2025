"""
Tests for calculate_and_print function and main function.
"""

import sys
import pytest
from main import calculate_and_print, main

@pytest.mark.parametrize("a_string, b_string, operation_string, expected_string", [
    ("5", "3", 'add', "The result of 5 add 3 is equal to 8"),
    ("10", "2", 'subtract', "The result of 10 subtract 2 is equal to 8"),
    ("4", "5", 'multiply', "The result of 4 multiply 5 is equal to 20"),
    ("20", "4", 'divide', "The result of 20 divide 4 is equal to 5"),
    ("1", "0", 'divide', "An error occurred: Cannot divide by zero"),
    ("9", "3", 'unknown', "Unknown operation: unknown"),
    ("a", "3", 'add', "Invalid number input: a or 3 is not a valid number."),
    ("5", "b", 'subtract', "Invalid number input: 5 or b is not a valid number."),
    ("1e100", "1e100", 'add', "The result of 1e100 add 1e100 is equal to 2E+100")
])
def test_calculate_and_print(a_string, b_string, operation_string, expected_string, capsys):
    """
    Test calculate_and_print for various inputs.
    """
    calculate_and_print(a_string, b_string, operation_string)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_string

def test_main_with_valid_args(capsys, monkeypatch):
    """
    Test main function with valid arguments.
    """
    test_args = ['main.py', '5', '3', 'add']
    monkeypatch.setattr(sys, 'argv', test_args)
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "The result of 5 add 3 is equal to 8"

def test_main_with_invalid_args(capsys, monkeypatch):
    """
    Test main function with invalid number of arguments.
    """
    test_args = ['main.py', '5', '3']
    monkeypatch.setattr(sys, 'argv', test_args)
    with pytest.raises(SystemExit) as excinfo:
        main()
    assert excinfo.value.code == 1
    captured = capsys.readouterr()
    assert captured.out.strip() == "Usage: python calculator_main.py <number1> <number2> <operation>"