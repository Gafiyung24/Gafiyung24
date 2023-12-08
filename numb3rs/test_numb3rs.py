import pytest
from numb3rs import validate

def test_validate():
    assert validate("255.1.2.3") == True
    assert validate("1000.400.300.500") == False
    assert validate("cat") == False
    assert validate("1.500.2000.1000") == False


