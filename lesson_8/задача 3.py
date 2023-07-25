import io
from contextlib import redirect_stdout

def eat_output(func):
    def wrapper(*args, **kwargs):
        with io.StringIO() as buf, redirect_stdout(buf):
            func(*args, **kwargs)
            return None
    return wrapper

@eat_output
def my_function():
    print("This output will be eaten")
