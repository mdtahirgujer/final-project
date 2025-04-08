def square_root(num):
    if num < 0:
        raise ValueError("Cannot compute square root of a negative number")
    result = (num + 1) // 2
    return result ** 2

try:
    print(square_root(-4))
except ValueError as e:
    print(e)
