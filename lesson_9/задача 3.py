import os

def ensure_file_exists(file_path):
    """
    Decorator that ensures that a specified file exists. If the file doesn't exist, it will create it.
    """
    def decorator(fn):
        def wrapper(*args, **kwargs):
            if not os.path.exists(file_path):
                open(file_path, 'a').close()

            return fn(*args, **kwargs)	
        return wrapper
    return decorator

@ensure_file_exists('test.txt')
def my_function():
    with open('test.txt', 'r') as f:
        print(f.read())

my_function()