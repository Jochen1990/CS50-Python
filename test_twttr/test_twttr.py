from twttr import shorten

def test_shorten():
    assert shorten("Twitter") == "Twttr"
    assert shorten("UlAra") == "lr"
    assert shorten("BGHIO") == "BGH"

def test_numbers():
    assert shorten("23jsdlui") == "23jsdl"

def test_punct():
    assert shorten("342.:hulu") == "342.:hl"
