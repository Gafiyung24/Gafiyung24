from fuel import convert, gauge
import pytest

def test_zerodivision():#test for zerodivisions
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("5/3")
    with pytest.raises(ValueError):
        convert("0.9/4")
    assert convert("1/4") != 25.00
"""def test_value():#test for non-integer entries
    with pytest.raises(ValueError):
        convert("cat/dog")"""
def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"


