import random
import names


class Login:
    username = "admin"
    password = "admin123"


class UsersCred:
    main_user_name = f"{names.get_first_name()}_{random.randint(0, 100)}"
    changed_user_name = f"{names.get_first_name()}_{random.randint(0, 100)}"
    password = 'qwerty123_45'