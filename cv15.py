def testing_priority(a, b):
    priority = []
    test1 = a + b * b
    test2 = a + b
    test2 *= b

    if test1 == test2:
        priority.append('+')
    else:
        priority.append('*')

    return priority

print(testing_priority(5, 10))