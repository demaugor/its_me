import time
import threading

def scheduled(interval, priority=0, stop_event=None):
    def decorator(fn):
        fn.priority = priority

        def wrapper(*args, **kwargs):
            while not stop_event.is_set():
                start_time = time.monotonic()
                fn(*args, **kwargs)
                end_time = time.monotonic()
                elapsed = end_time - start_time
                remaining_time = interval - elapsed
                stop_event.wait(max(remaining_time, 1))

        return wrapper

    return decorator


stop_event = threading.Event()

@scheduled(interval=5, priority=1, stop_event=stop_event)
def my_function():
    print("My function is running on schedule!")

try:
    while True:
        pass
except KeyboardInterrupt:
    stop_event.set()
    print('KeyboardInterrupt: stopping execution of scheduled tasks.')