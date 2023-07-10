from project import request, validate, user
import pytest

def test_request():
    response = request("48.137154", "11.576124", "today")
    assert response.status_code == 200

def test_validate():
    assert validate("2023-04-12") == True
    assert validate("sdfs") == False
    assert validate("2023-17-03") == False