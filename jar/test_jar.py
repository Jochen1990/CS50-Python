from jar import Jar
import pytest


def test_init():
    jar = Jar()

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪🍪"


def test_withdraw():
    jar = Jar()
    jar.deposit(4)
    jar.withdraw(3)
    assert str(jar) == "🍪"
    jar.withdraw(1)
    assert str(jar) == ""
    jar.deposit(6)
    jar.withdraw(3)
    assert str(jar) == "🍪🍪🍪"



