from logging import exception


def triangle(side1, side2, x):
    if x == 'a' or x == 'b':
        side3 = (abs(side1**2 - side2**2))**(1/2)
    elif x == 'c':
        side3 = (side1**2 + side2**2)**(1/2)
    else:
        raise exception('wrong name of side')

    return side3

print(triangle(8, 10, 'a'))