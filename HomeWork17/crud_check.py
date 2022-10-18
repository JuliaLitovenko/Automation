import pytest
import requests
import json
import random

# values
headers = {
    'Content-Type': 'application/json'
}
urls = ["https://www.aqa.science/users/"]


@pytest.fixture
def ses_class():
    pass


@pytest.fixture
def login_logout_func():
    pass


def test_create_user_api(cred_file):
    # Create user
    payload = json.dumps({
        "username": f"Uswer_{random.randint(0, 100)}",
        "email": f"{random.randint(0, 100)}@rrr.com",
        "groups": []
    })
    response = requests.request("POST", urls[0], auth=cred_file, data=payload, headers=headers).json()
    with open('added_user.json', "w") as f:
        json.dump(response, f)
    assert response["url"] is not None, "User not created"


def test_read_user_api(check_user, user_data):
    # find created user in users list
    with open('users_list.json', 'r') as f:
        data = json.load(f)
    value = ""
    for item in data:
        if item.get("url", None) == user_data:
            value += item.get("url")
    assert value == user_data, "User not found"


def test_update_user_api(user_data, cred_file):
    # update created user
    payload = json.dumps({
        "url": user_data,
        "username": f"Uswer_{random.randint(0, 100)}",
        "email": f"{random.randint(0, 100)}@rrr.com",
        "groups": []
    })
    response = requests.request("PATCH", user_data, auth=cred_file, headers=headers, data=payload)
    assert response.status_code == 200, "User not updated"


def test_delete_user_api(user_data, cred_file):
    # delete created user and erase file added_user.json
    response = requests.request("DELETE", user_data, auth=cred_file)
    open('added_user.json', 'w').close()
    assert response.status_code == 204, "User not deleted"
