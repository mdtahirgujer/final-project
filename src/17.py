import numpy as np

# Example code snippet with comments
def greet():
    print("Hello World")

greet()

def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

numbers = [1, 2, 3]
result = calculate_sum(numbers)
print(f"The sum of the numbers is: {result}")
