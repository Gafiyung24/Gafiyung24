import pytest
from working import convert

#test for pattern 5:00 AM to 5:00 PM
def test_p1():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
def test_ValueError1():
    with pytest.raises(ValueError):
        convert("9:00 AM to 17:00 PM")
    with pytest.raises(ValueError):
        convert("9:65 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM to 5:70 PM")
def test_ValueError2():
    with pytest.raises(ValueError):
        convert("9:00 to 5:00")
    with pytest.raises(ValueError):
        convert("9 AM to 5:00")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("9 to 5 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM - 5:00 PM")
