from plates import is_valid

def test_allalpha():
    assert isvalid("CS") == True
    assert isvalid("HELLO") == True
    assert isvalid("GOODBYE") == False

def test_alnum():
    assert isvalid("CS50") == True
    assert isvalid("CS05") == False
    assert isvalid("GA55A") == False
    assert isvalid("50") == False
def test_mark():
    assert isvalid("HELLO, GOODBYE") == False

