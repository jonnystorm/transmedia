#-*- coding: utf-8 -*-
#
# Copyright © 2014 Jonathan Storm <the.jonathan.storm@gmail.com>
# This work is free. You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar. See the COPYING.WTFPL file for more details.

__author__ = 'jstorm'

import transmedia.codecs as codecs
from transmedia.util import Pixel


### simple_encode tests ###

def check_simple_encode_maps_word_to_correct_color(word, correct_color):
    test_color = codecs.SimpleCodec.encode(word).as_integer_triple()

    assert test_color == correct_color, \
        "{} != {}".format(test_color, correct_color)


def test_simple_encode_maps_words_to_correct_colors():
    values = ((bytearray.fromhex('0000'), (int(0x00), int(0x00), int(0x00))),
              (bytearray.fromhex('1111'), (int(0x11), int(0x11), int(0x00))),
              (bytearray.fromhex('ffff'), (int(0x00), int(0x01), int(0xff))))

    for word, correct_color in values:
        yield(check_simple_encode_maps_word_to_correct_color, word,
              correct_color)


def test_simple_encode_raises_value_error_on_single_byte_input():
    try:
        codecs.SimpleCodec.encode(bytearray.fromhex('00'))

        assert False, "simple_encoder erroneously succeeds on single-byte input"

    except ValueError:
        pass


def test_simple_encode_raises_type_error_on_int_input():
    try:
        codecs.SimpleCodec.encode(1)

        assert False, "simple_encoder erroneously succeeds on integer input"

    except TypeError:
        pass


### simple_decode tests ###

def check_simple_decode_maps_color_to_correct_word(color, correct_word):
    test_word = codecs.SimpleCodec.decode(Pixel(*color))

    assert test_word == correct_word, "{} != {}".format(test_word, correct_word)


def test_simple_decode_maps_colors_to_correct_words():
    values = ((bytearray.fromhex('0000'), (int(0x00), int(0x00), int(0x00))),
              (bytearray.fromhex('1111'), (int(0x11), int(0x11), int(0x00))),
              (bytearray.fromhex('ffff'), (int(0x00), int(0x01), int(0xff))))

    for correct_word, color in values:
        yield(check_simple_decode_maps_color_to_correct_word, color,
              correct_word)
