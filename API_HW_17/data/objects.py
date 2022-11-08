class LoginPage:
    username_id = '//*[@id="id_username"]'
    pswd_id = '//*[@id="id_password"]'
    submit_btn = '//*[@id="login-form"]/div[3]/input'


class AdminPage(LoginPage):
    admin_page_header_id = '//*[@id="site-name"]/a'
    logout_id = '//*[@id="user-tools"]/a[3]'
    log_again_id = '//*[@id="content"]/p[2]/a'


class CreateUsers:
    add_usr_id = '//*[@id="content-main"]/div/table/tbody/tr[2]/td[1]/a'
    username_id = '//*[@id="id_username"]'
    password_id = '//*[@id="id_password1"]'
    confirm_pswd_id = '//*[@id="id_password2"]'
    save_id = '//*[@id="user_form"]/div/div/input[1]'
    success_id = '//*[@id="content"]/h2'


class UpdateUsers:
    first_name_id = '//*[@id="id_first_name"]'
    last_name_id = '//*[@id="id_last_name"]'
    save_btn_id = '//*[@id="user_form"]/div/div/input[1]'


class FindUsers:
    users_id = '//*[@id="content-main"]/div/table/tbody/tr[2]/th/a'
    find_field_id = '//*[@id="searchbar"]'
    found_username = '//*[@id="result_list"]/tbody/tr/th/a'


class DeleteUsers:
    delete_btn_id = '//*[@id="user_form"]/div/div/p/a'
    confirm_delete_id = '//*[@id="content"]/form/div/input[2]'
    count_users_id = '//*[@id="changelist-form"]/p'