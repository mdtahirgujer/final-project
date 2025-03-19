import random
def get_random_python_code():
    # Generate a random number between 1 and 10
    num = random.randint(1, 10)
    if num <= 3:
        return "print('Hello World!')"
    elif num <= 6:
        return "for i in range(5):\n\tprint(i)"
    else:
        return "while True:\n\tprint('Hello World!')"