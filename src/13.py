import random

def get_random_code():
    # Generate a random 4-digit number between 1000 and 9999
    rand_num = str(random.randint(1000, 9999))
    # Check if the number is already in use
    while rand_num in used_codes:
        # If it is, generate a new random number
        rand_num = str(random.randint(1000, 9999))
    # Add the new code to the list of used codes
    used_codes.append(rand_num)
    return rand_num