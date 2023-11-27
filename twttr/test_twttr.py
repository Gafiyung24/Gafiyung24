from twttr import shorten

def test_word():
    assert shorten("already") == "lrdy"
    assert shorten("EvangElIsm") == "vnglsm"

def test_numbers():
    assert shorten("5dream") == "5drm"

def test_punc():
    assert shorten("Femi.,d") == "Fm.,d"
    

