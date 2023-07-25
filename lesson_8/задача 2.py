def authenticate(func):
    def wrapper(*args, **kwargs):
        if not wrapper.authenticated:
            username = input("Введите имя пользователя: ")
            password = input("Введите пароль: ")
            if authenticate_user(username, password):
                wrapper.authenticated = True
            else:
                print("Ошибка: неверное имя пользователя или пароль.")
                return
        return func(*args, **kwargs)
    wrapper.authenticated = False
    return wrapper


def authenticate_user(username, password):
    
    users = {
        "danil": "12345",
        "timur": "qwerty",
    }
    return users.get(username) == password


@authenticate
def sensitive_operation():
    print("Выполняю чувствительную операцию.")


sensitive_operation()  
  