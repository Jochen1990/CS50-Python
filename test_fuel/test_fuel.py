from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("1/4") == 25
    assert convert("3/4") == 75
    assert convert("0/8") == 0
    with pytest.raises(ValueError):
        assert convert("5/4")
    with pytest.raises(ValueError):
        assert convert("cat/dog")
    with pytest.raises(ZeroDivisionError):
        assert convert("5/0")


def test_gauge():
    assert gauge(0) == "E"
    assert gauge(100) == "F"
    assert gauge(75) == "75%"
    assert gauge(80) == "80%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
