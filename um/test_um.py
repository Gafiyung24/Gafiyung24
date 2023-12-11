from um import count
import pytest

def test_type1():
    assert count("hello, um") == 1
    assert count("um hello, um") == 2
    assert count("um try um, um") == 3
def test_type2():
    assert count("UM please") == 1
    assert count("UM UM thanks") == 2
def test_type3():
    assert count("Um, UM, um") == 3
    assert count("uM, um, UM") == 3
def test_type4():
    assert count("yummy, tummy, fummy") == 0
