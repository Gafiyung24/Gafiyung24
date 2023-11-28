from fuel import convert, gauge
import pytest

def test_zerodivision():#test for zerodivisions
    with pytest.raises(ZeroDivisionError):
        convert("5/0")
def test_value():#test for non-integer entries
    with pytest.raises(ValueError):
        convert("cat/dog")
def test_gauge():
    assert gauge(0.5) == "E"
    assert gauge(1) == "E"
    assert gauge(99.5) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"


