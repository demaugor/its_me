def call_once(func):
    def wrapper(*args, **kwargs):
        if not wrapper.called:
            wrapper.called = True
            return func(*args, **kwargs)
        else:
            print("Ошибка: функция уже была вызвана.")
    wrapper.called = False
    return wrapper

@call_once
def hello(name):
    print(f"Привет, {name}!")

hello("Алиса")  # Выводит "Привет, Алиса!"
hello("Боб")  # Выводит "Ошибка: функция уже была вызвана."