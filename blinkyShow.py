#!/usr/bin/env python

from blinkstick import blinkstick
import random


def get_random_colour():
    r = lambda: random.randint(0, 255)
    return '#%02X%02X%02X' % (r(), r(), r())

def main():
    colour_hex = get_random_colour()
    for bstick in blinkstick.find_all():
        for i in range(8):
            bstick.set_color(index=i, hex=colour_hex)
            print bstick.get_serial() + " " + bstick.get_color(color_format="hex")


if __name__ == '__main__':
    main()