def add_numbers(a, b):
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a

print('printing', add_numbers(1, 11))