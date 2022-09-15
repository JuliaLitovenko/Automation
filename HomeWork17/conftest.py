import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from data.links import Main_Page_URl
from data.page_objects import MainPage, UserPage, ChangeUserPage, LoginPage, UsersCred

with open(
        "resources/data.json",
        "r") as f:
    secret_variables = json.load(f)

options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')


s = Service('C:/Users/yuliia.litovenko/PycharmProjects/Automation/venv/chromedriver.exe')
driver = webdriver.Chrome(service=s)


driver.get(secret_variables['access_url'])
name_field = driver.find_element(By.ID, LoginPage.login_field_id)
password_field = driver.find_element(By.XPATH, LoginPage.password_field_id)
submit_button = driver.find_element(By.XPATH, LoginPage.submit_button_id)

name_field.send_keys(secret_variables["login"])
time.sleep(1)
password_field.send_keys(secret_variables["password"])

submit_button.click()

element_fo_found = driver.find_element(By.XPATH,
                                       MainPage.page_header_id)
assert element_fo_found.text == "Django administration"

def test_add_user():

 if UsersCred.main_user_name not in get_all_users_list():
     driver.get(Main_Page_URl)
     driver.find_element(By.XPATH, MainPage.user_list_button).click()
     driver.find_element(By.XPATH, UserPage.add_user_button).click()
     driver.find_element(By.XPATH, UserPage.user_name_field).send_keys(UsersCred.main_user_name)
     driver.find_element(By.XPATH, UserPage.password_field).send_keys(UsersCred.password)
     driver.find_element(By.XPATH, UserPage.password_confirmation_field).send_keys(UsersCred.password)
     driver.find_element(By.XPATH, UserPage.save_button).click()
 else:
     test_add_user()

 assert UsersCred.main_user_name in get_all_users_list()

def test_upd_user():

 driver.get(Main_Page_URl)
 driver.find_element(By.XPATH, MainPage.user_list_button).click()
 driver.find_element(By.XPATH, UserPage.search_field).send_keys(UsersCred.main_user_name)
 driver.find_element(By.XPATH, UserPage.search_button).click()
 driver.find_element(By.XPATH, UserPage.user_data).click()
 driver.find_element(By.XPATH, ChangeUserPage.user_name_field).clear()
 driver.find_element(By.XPATH, ChangeUserPage.user_name_field).send_keys(UsersCred.changed_user_name)
 driver.find_element(By.XPATH, ChangeUserPage.save_button).click()

 assert UsersCred.changed_user_name in get_all_users_list()



def test_del_usr():

 driver.get(Main_Page_URl)
 driver.find_element(By.XPATH, MainPage.user_list_button).click()
 driver.find_element(By.XPATH, UserPage.search_field).send_keys(UsersCred.changed_user_name)
 driver.find_element(By.XPATH, UserPage.search_button).click()
 driver.find_element(By.XPATH, UserPage.user_data).click()
 driver.find_element(By.XPATH, ChangeUserPage.delete_button).click()
 driver.find_element(By.XPATH, ChangeUserPage.submit_delete_button).click()

 assert UsersCred.changed_user_name not in get_all_users_list()



def get_all_users_list():

    driver.get(Main_Page_URl)
    driver.find_element(By.XPATH, MainPage.user_list_button).click()
    users_list_elem = driver.find_elements(By.XPATH, UserPage.user_data)
    users_list = []
    for i in users_list_elem:
        users_list.append(i.text)
        return users_list

