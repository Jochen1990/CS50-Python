from plates import is_valid

def test_letters():
    assert is_valid("61") == False
    assert is_valid("03") == False
    assert is_valid("7h") == False
    assert is_valid("CS50") == True

def test_numchars():
    assert is_valid("AA") == True
    assert is_valid("AAAAAAA") == False
    assert is_valid("323mklksd") == False
    assert is_valid("GOODBYE") == False

def test_numbers():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False
    assert is_valid("AAA022") == False

def test_punct():
    assert is_valid("AA.,") == False
    assert is_valid("-jal") == False
    assert is_valid("CS50.") == False
    assert is_valid("/CS50") == False