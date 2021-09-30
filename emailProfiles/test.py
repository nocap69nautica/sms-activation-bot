def count(func):
    def wrapper(*args, **kwargs):
        wrapper.counter += 1    # executed every time the wrapped function is called
        return func(*args, **kwargs)
    wrapper.counter = 0         # executed only once in decorator definition time
    return wrapper


@count
def func():
    pass


def count():
    if func:
        return func.counter


count()
