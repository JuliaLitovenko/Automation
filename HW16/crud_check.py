import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from data.links import Main_Page_URl
from data.page_objects import MainPage, UserPage, ChangeUserPage, UsersCred, LoginPage


def test_login():
    pytest.driver.get(pytest.secret_variables['endpoint'])
    name_field = pytest.driver.find_element(By.ID, LoginPage.login_field_id)
    password_field = pytest.driver.find_element(By.XPATH, LoginPage.password_field_id)
    submit_button = pytest.driver.find_element(By.XPATH, LoginPage.submit_button_id)

    name_field.send_keys(pytest.secret_variables["login"])
    time.sleep(1)
    password_field.send_keys(pytest.secret_variables["password"])
    submit_button.click()
    element_fo_found = pytest.driver.find_element(By.XPATH,
                                       MainPage.page_header_id)
    assert element_fo_found.text == "Django administration"

# Add user
def test_create_user():
    pytest.driver.get(Main_Page_URl)
    pytest.driver.find_element(By.XPATH, MainPage.user_list_button).click()
    time.sleep(1)
    pytest.driver.find_element(By.XPATH, UserPage.add_user_button).click()
    time.sleep(1)
    pytest.driver.find_element(By.XPATH, UserPage.user_name_field).send_keys(UsersCred.main_user_name)
    time.sleep(1)
    pytest.driver.find_element(By.XPATH, UserPage.password_field).send_keys(UsersCred.password)
    time.sleep(1)
    pytest.driver.find_element(By.XPATH, UserPage.password_confirmation_field).send_keys(UsersCred.password)
    time.sleep(1)
    pytest.driver.find_element(By.XPATH, UserPage.save_button).click()
    time.sleep(5)

#Update user info
def test_update_user():
    pytest.driver.get(Main_Page_URl)
    pytest.driver.find_element(By.XPATH, MainPage.user_list_button).click()
    time.sleep(1)
    pytest.driver.find_element(By.XPATH, UserPage.search_field).send_keys(UsersCred.main_user_name)
    time.sleep(1)
    pytest.driver.find_element(By.XPATH, UserPage.search_button).click()
    time.sleep(1)
    pytest.driver.find_element(By.XPATH, UserPage.user_data).click()
    time.sleep(1)
    pytest.driver.find_element(By.XPATH, ChangeUserPage.user_name_field).clear()
    time.sleep(1)
    pytest.driver.find_element(By.XPATH, ChangeUserPage.user_name_field).send_keys(UsersCred.changed_user_name)
    time.sleep(1)
    pytest.driver.find_element(By.XPATH, ChangeUserPage.save_button).click()
    time.sleep(5)

# Delete user
def test_delete_user():
    pytest.driver.get(Main_Page_URl)
    pytest.driver.find_element(By.XPATH, MainPage.user_list_button).click()
    time.sleep(1)
    pytest.driver.find_element(By.XPATH, UserPage.search_field).send_keys(UsersCred.changed_user_name)
    time.sleep(1)
    pytest.driver.find_element(By.XPATH, UserPage.search_button).click()
    time.sleep(1)
    pytest.driver.find_element(By.XPATH, UserPage.user_data).click()
    time.sleep(1)
    pytest.driver.find_element(By.XPATH, ChangeUserPage.delete_button).click()
    time.sleep(1)
    pytest.driver.find_element(By.XPATH, ChangeUserPage.submit_delete_button).click()

#Get all users
def get_all_users():
    pytest.driver.get(Main_Page_URl)
    pytest.driver.find_element(By.XPATH, MainPage.user_list_button).click()
    time.sleep(1)
    users_list_elem = pytest.driver.find_elements(By.XPATH, UserPage.user_data)
    users_list = []
    for i in users_list_elem:
        users_list.append(i.text)
    pytest.driver.close()







