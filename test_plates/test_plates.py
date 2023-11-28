from plates import is_valid

def test_allalpha():
    assert isvalid("CS50") == True
    assert isvalid("HELLO") == True
    assert isvalid("GOODBYE") == True
    