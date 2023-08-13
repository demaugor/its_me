import time

def rate_limiter(limit):
       
    def decorator(fn):
        last_call = 0
        def wrapper(*args, **kwargs):
            nonlocal last_call
            elapsed = time.time() - last_call
            if elapsed < limit:
                raise Exception(f"Rate limit exceeded. Wait {limit - elapsed:.2f} seconds before trying again.")
            result = fn(*args, **kwargs)
            last_call = time.time()
            return result
        return wrapper
    return decorator

@rate_limiter(limit=5)
def my_function():
    print("Hello, world!")

if __name__ == "__main__":
    my_function() # вызываем функцию здесь
    
    
