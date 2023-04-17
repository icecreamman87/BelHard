#Task_1
def check_login(name, password, try_count=3, lockout_message="Система заблокирована. Повторите попытку через 5 мин."):
    authorized = False
    while try_count > 0 and not authorized:
        name = input("Введите ваш логин: ")
        password = input("Введите ваш пароль: ")
        if '*' not in name and ',' not in name and '/' not in name and len(password) >= 6:
            authorized = True
            print("Добро пожаловать в систему")
        else:
            try_count -= 1
            print(f"Неправильный логин или пароль, осталось {try_count} попыток")
    if not authorized:
        print(lockout_message)


check_login('name', 'password')