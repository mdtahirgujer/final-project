import random

def get_random_code():
    code = "".join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") for i in range(8))
    return code
