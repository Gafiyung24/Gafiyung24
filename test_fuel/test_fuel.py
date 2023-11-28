from fuel import convert, guage

def test_zerodivision():
    with pytest.raises(ZeroDivisionError):
        convert("5/0")
def test_value():
    with pytest.raise

