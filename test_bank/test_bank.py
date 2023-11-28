from bank import value

def test_hello():
    assert value("hello Sam") == "$0"
    assert value("hello Gaffy") == "$0"
def test_h():
    assert value("hi Sam") == "$20"
    assert value("hey Gaffy") == "$20"
def test_others():
    assert value("What's up?") == "$100"
    assert value("what's happening?") == "$100"
def test_none():
    assert value("") == "$100"
