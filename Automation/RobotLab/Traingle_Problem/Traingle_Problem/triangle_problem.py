# MY_NAME = ADEKUNLE_JOHN

def side(x, y, z):
    if x == y == z:
        return 'equilateral'

    elif x == y or y == z or z == x:
        return 'isosceles'

    else:
        return 'irregular'
