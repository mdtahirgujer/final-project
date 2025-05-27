def sum_of_squares(n):
    total = 0
    for i in range(1, n + 1):
        total += i * i
    return total

n = 5
print(sum_of_squares(n))  # Output: 55
