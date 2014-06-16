#-*- coding: utf-8 -*-
#
# Copyright © 2014 Jonathan Storm <the.jonathan.storm@gmail.com>
# This work is free. You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar. See the COPYING.WTFPL file for more details.

__author__ = 'jstorm'

from transmedia.util import Pixel


class SimpleCodec():
    """Turns two-byte words into integer triples or vice versa. The provided
    methods, at two bytes per 24-bit pixel, are inefficient but direct and
    lossless."""
    @staticmethod
    def encode(word):
        """Given two bytes interpreted as a 16-bit signed int, if the value is
        positive, assign the first byte to the red channel, and the second, to
        the green one, then set the blue channel to zero. If the value is
        negative, take the two's complement prior to channel assignment and set
        the blue channel to 255.

        :param word: two bytes representing a 16-bit signed int
        :type word: bytes()

        :return: a pixel object
        :rtype: Pixel()
        """
        if word[0] & 2**7:
            red = word[1] ^ 255
            green = (word[0] ^ 255) + 1
            blue = 255
        else:
            red, green = word
            blue = 0

        return Pixel(red, green, blue)

    @staticmethod
    def decode(pixel):
        """Given a pixel object, if blue != 255, return r and g, concatenated in
        a bytearray. Otherwise, if b == 255, treat r and g as a signed, 16-bit
        integer, taking the little-endian two's complement and returning the
        result.

        :param pixel: a pixel object
        :type pixel: Pixel()

        :return: a word (two bytes)
        :rtype: bytes()
        """
        if pixel.blue == 255:
            word = bytearray([(pixel.green ^ 255) + 1])
            word += bytearray([pixel.red ^ 255])
        else:
            word = bytearray([pixel.red, pixel.green])

        return word
