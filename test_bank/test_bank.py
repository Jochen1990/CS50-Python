from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0

def test_h():
    assert value("huibu") == 20
    assert value("Huibu") == 20
    assert value("Hollaa") == 20

def test_def():
    assert value("") == 100
    assert value("123123.") == 100
    assert value(".sjd") == 100
    assert value("ahaa") == 100