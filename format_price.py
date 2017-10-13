import math


def get_thousands(int_value):
    thousands = []
    i = 0
    while int_value:
        thousands.append(int(int_value % 1000))
        int_value = int_value // 1000
    return thousands


def format_price(price):
    try:
        (fract, int_value) = math.modf(price)
        thousands = get_thousands(int_value)
        if round(fract, 2) > 0:
            thousands[0] += round(fract, 2)
        return ' '.join(map(str, reversed(thousands)))
    except TypeError as e:
        print(str(e))



if __name__ == '__main__':
    print(format_price(1555323444.234))
