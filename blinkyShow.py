#!/usr/bin/env python

from blinkstick import blinkstick
import random
import sys
import re

RED_HEX = '#ff0000'


def get_random_colour():
    r = lambda: random.randint(0, 255)
    return '#%02X%02X%02X' % (r(), r(), r())


def check_hex_arg(hex_arg):
    match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', hex_arg)

    if match:
        return True

    else:
        return False


def main():
    global colour_hex
    colour_hex = RED_HEX
    if sys.argv[1] == 'random':
        colour_hex = get_random_colour()
    else:
        if check_hex_arg(sys.argv[1]):
            colour_hex = sys.argv[1]
        else:
            raise ValueError('not valid colour hex, try again')

    for bstick in blinkstick.find_all():
        for i in range(8):
            bstick.set_color(index=i, hex=colour_hex)
            print bstick.get_serial() + " " + bstick.get_color(color_format="hex")


if __name__ == '__main__':
    main()