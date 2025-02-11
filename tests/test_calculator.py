'''Calculator tests'''
from calculator import Calculator

def test_addition():
    '''Test addition function'''    
    assert Calculator.add(2, 2) == 4

def test_subtraction():
    '''Test subtraction function'''    
    assert Calculator.subtract(2, 2) == 0

def test_divide():
    '''Test division function'''    
    assert Calculator.divide(2, 2) == 1

def test_multiply():
    '''Test multiplication function'''    
    assert Calculator.multiply(2, 2) == 4