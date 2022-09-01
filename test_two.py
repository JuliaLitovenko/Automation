import pytest
import requests

def test_first():
    response = requests.get("https://www.amazon.com/lol")
    assert response.status_code == 404


def test_sec():
    response = requests.post("https://industrial.ubidots.com/api/v1.6/devices/DEVICE-LABEL/?token=TOKEN&_method=post&VARIABLE-LABEL=1")
    assert response.status_code == 401


def test_three():
    response = requests.get("http://api.zippopotam.us/us/90210")
    assert response.headers["Content-Type"] == "application/json"
    print(response)