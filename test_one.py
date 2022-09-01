import pytest
import requests

def test_first():
    response = requests.get("https://www.python.org/")
    print("checking response code")
    assert response.status_code == 200


def test_sec():
    response = requests.get("https://www.python.org/11444222")
    assert response.status_code != 200

def test_third():
    response = requests.get("http://api.zippopotam.us/us/90210")
    assert response.status_code == 200