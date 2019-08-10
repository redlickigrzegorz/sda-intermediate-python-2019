import functools
import time


def time_it(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'"{func.__name__}" took {(end - start):.8f} s.')
        return result
    return wrapper

@time_it
def hello():
    return "I'm from hello function"
@time_it
def hello_with_delay(sek):
    time.sleep(sek)
    return "I'm from hello_with_delay function"

if __name__ == '__main__':
    print(hello())
    print(hello_with_delay(2))
