import random
import time


def retry(tries=3, delay=1, exceptions=(Exception,)):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempt = 0
            while attempt < tries:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempt += 1
                    print(f"Attempt {attempt} failed: {e} retrying in {delay} seconds...")
                    time.sleep(delay)
            raise

        return wrapper

    return decorator


@retry()
def unreliable_network_call():
    if random.random() < 0.7:
        raise ConnectionRefusedError('Connection Failed')
    return 'Data Successfully fetched!'


print(unreliable_network_call())
