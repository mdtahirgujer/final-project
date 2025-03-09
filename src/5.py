import random

def get_random_code(length):
    characters = 'abcdefghijklmnopqrstuvwxyz'
    code = ''
    for i in range(length):
        code += random.choice(characters)
    return code