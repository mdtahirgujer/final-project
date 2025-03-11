import random

def get_random_code():
    return "".join([chr(random.randint(65, 90)) for i in range(10)])
