from plates import is_valid

def test_allalpha():
    assert isvalid("CS") == True
    assert isvalid("HELLO") == True
    assert isvalid("GOODBYE") == False
    assert isvalid("GA55A") == False

