from seasons import convert
import pytest

def test_convert():
    assert convert("2022-04-18") == "Five hundred twenty-five thousand, six hundred minutes"
    assert convert("2021-04-18") == "One million, fifty-one thousand, two hundred minutes"
    with pytest.raises(SystemExit):
        assert convert("sdfgsdg")

