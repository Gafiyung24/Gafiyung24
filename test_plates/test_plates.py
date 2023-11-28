from plates import is_valid

def test_allalpha():
    assert is_valid("CS") == True
    assert is_valid("HELLO") == True
    assert is_valid("GOODBYE") == False

def test_alnum():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("GA55A") == False
    assert is_valid("50") == False
def test_mark():
    assert is_valid("HELLO, GOODBYE") == False
    assert is_valid("GA.50") == False

