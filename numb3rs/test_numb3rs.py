from numb3rs import validate
import pytest

def test_validate1():
    assert validate("255.255.255.255") == True
    assert validate("127.0.0.1") == True
    assert validate("1.2.255.255") == True
    assert validate("78.255.4.255") == True


def test_validate2():
    assert validate("512.512.512.512") == False
    assert validate("0.1") == False
    assert validate("cat") == False
    assert validate("78.255.4.") == False
    assert validate("78.bloodymary.4.255") == False
    assert validate("255.512.512.512") == False
