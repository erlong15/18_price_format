import math
import argparse


def get_thousands(int_value):
    thousands = []
    i = 0
    while int_value:
        thousands.append(int(int_value % 1000))
        int_value = int_value // 1000
    return thousands


def format_price(price):
    if type(price) not in (int, float) or price <= 0:
        return "Цена уточняется"
    (fract, int_value) = math.modf(price)
    thousands = get_thousands(int_value)
    if round(fract, 2) > 0:
        thousands[0] += round(fract, 2)
    return ' '.join(map(str, reversed(thousands)))


def get_args():
    parser = argparse.ArgumentParser(description='Price formatter.')
    parser.add_argument('price', help='price for formatting',
                        type=float)
    return parser.parse_args()


if __name__ == '__main__':
    args = get_args()
    print(format_price(args.price))
