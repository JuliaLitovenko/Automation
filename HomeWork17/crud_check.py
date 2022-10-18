import time
import pytest
from selenium.webdriver.common.by import By
from tests.data.locators import CreateUsers, UpdateUsers, DeleteUsers


def test_create_user():
    # Create user
    add_user = pytest.driver.find_element(By.XPATH, CreateUsers.add_usr_id)
    add_user.click()

    create_username = pytest.driver.find_element(By.XPATH, CreateUsers.username_id)
    create_password = pytest.driver.find_element(By.XPATH, CreateUsers.password_id)
    create_conf_password = pytest.driver.find_element(By.XPATH, CreateUsers.confirm_pswd_id)
    create_save = pytest.driver.find_element(By.XPATH, CreateUsers.save_id)

    create_username.send_keys(pytest.secret_variables["username"])
    create_password.send_keys(pytest.secret_variables["password"])
    create_conf_password.send_keys(pytest.secret_variables["password"])
    create_save.click()


def test_read_user(find_func):
    # Check success of creation
    success_create = pytest.driver.find_element(By.XPATH, CreateUsers.success_id)
    assert success_create.text == pytest.secret_variables["username"], print("User didn't created")


def test_update_user(find_func):
    # Update user
    first_name = pytest.driver.find_element(By.XPATH, UpdateUsers.first_name_id)
    last_name = pytest.driver.find_element(By.XPATH, UpdateUsers.last_name_id)
    save_updates = pytest.driver.find_element(By.XPATH, UpdateUsers.save_btn_id)

    first_name.send_keys(pytest.secret_variables["first_name"])
    last_name.send_keys(pytest.secret_variables["last_name"])
    time.sleep(3)
    save_updates.click()


def test_delete_user(find_func):
    # Delete user
    delete_user = pytest.driver.find_element(By.XPATH, DeleteUsers.delete_btn_id)
    delete_user.click()
    time.sleep(4)

    confirm_delete = pytest.driver.find_element(By.XPATH, DeleteUsers.confirm_delete_id)
    confirm_delete.click()

    # Check success of deletion
    count_users = pytest.driver.find_element(By.XPATH, DeleteUsers.count_users_id)
    assert count_users.text == '0 users', print("User didn't deleted")
