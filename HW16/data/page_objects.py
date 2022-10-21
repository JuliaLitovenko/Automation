import random
import names

class LoginPage:
    submit_button_id = '//*[@id="login-form"]/div[3]/input'
    login_field_id = 'id_username'
    password_field_id = '//*[@id="id_password"]'


class MainPage:
    page_header_id = '//*[@id="site-name"]/a'
    user_list_button = '//*[@id="content-main"]/div/table/tbody/tr[2]/th/a'


class UserPage:
    add_user_button = '//*[@id="content-main"]/ul/li/a'
    user_name_field = '//*[@id="id_username"]'
    password_field = '//*[@id="id_password1"]'
    password_confirmation_field = '//*[@id="id_password2"]'
    save_button = '//*[@id="user_form"]/div/div/input[1]'
    successful_message = '//*[@id="main"]/div/ul/li'
    search_field = '//*[@id="searchbar"]'
    search_button = '//*[@id="changelist-search"]/div/input[2]'
    search_result = '//*[@id="changelist-search"]/div/span'
    user_data = '//*[@id="result_list"]/tbody/tr/th/a'


class ChangeUserPage:
    user_name_field = '//*[@id="id_username"]'
    save_button = '//*[@id="user_form"]/div/div/input[1]'
    delete_button = '//*[@id="user_form"]/div/div/p/a'
    submit_delete_button = '//*[@id="content"]/form/div/input[2]'

class UsersCred:
    main_user_name = f"user111_{random.randint(0, 100)}"
    changed_user_name = f"user5555_{random.randint(0, 100)}"
    password = 'Test!123'