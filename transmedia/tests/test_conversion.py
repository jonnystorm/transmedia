#-*- coding: utf-8 -*-
#
# Copyright © 2014 Jonathan Storm <the.jonathan.storm@gmail.com>
# This work is free. You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar. See the COPYING.WTFPL file for more details.

__author__ = 'jstorm'

import io

import transmedia.bytes2png as pcm2png
import transmedia.png2bytes as png2pcm
import transmedia.encoders as encoders


test_data = bytearray.fromhex('ffff6d06cb0cc436103c2741895c1f5f4861')


### words2pixels tests ###

def check_words2pixels_returns_correct_width(correct_width):
    test_data_file = io.BytesIO(test_data)
    rows = pcm2png.words2pixels(test_data_file, correct_width,
                                encoders.simple_encode)

    byte_depth = 3
    width_top = len(rows[0]) / byte_depth
    width_bottom = len(rows[-1]) / byte_depth

    assert width_top == width_bottom == correct_width, \
        "({} == {} == {}) is false".format(width_top, width_bottom,
                                           correct_width)


def test_words2pixels_returns_correct_width():
    for width in (1, 3, 9):  # a single column, a square, a single row
        yield check_words2pixels_returns_correct_width, width


def test_words2pixels_returns_square():
    correct_dimension = 3  # 3x3 square
    test_data_file = io.BytesIO(test_data)
    rows = pcm2png.words2pixels(test_data_file, correct_dimension,
                                encoders.simple_encode)

    byte_depth = 3
    width_top = len(rows[0]) / byte_depth
    height = len(rows)

    assert width_top == height == correct_dimension, \
        "({} == {} == {} == {}) is false".format(width_top, height,
                                                 correct_dimension)


def test_words2pixels_raises_runtime_error_on_negative_width():
    try:
        negative_width = -1
        file = io.BytesIO(test_data)
        pcm2png.words2pixels(file, negative_width, encoders.simple_encode)

        assert False, "words2pixels erroneously succeeds on negative width"

    except RuntimeError:
        pass


def test_words2pixels_raises_runtime_error_on_zero_width():
    try:
        zero_width = 0
        file = io.BytesIO(test_data)
        pcm2png.words2pixels(file, zero_width, encoders.simple_encode)

        assert False, "words2pixels erroneously succeeds on zero width"

    except RuntimeError:
        pass


def test_words2pixels_returns_max_width_on_excessive_width_input():
    excessive_width = len(test_data) // 2 + 1  # max width + 1
    test_data_file = io.BytesIO(test_data)
    rows = pcm2png.words2pixels(test_data_file, excessive_width,
                                encoders.simple_encode)

    byte_depth = 3
    actual_width = len(rows[0]) / byte_depth

    assert actual_width != excessive_width, \
        "{} == {} == {}".format(actual_width, excessive_width)


### pixels2words tests ###

def test_pixels2words_returns_correct_length():
    correct_length = len(test_data)
    byte_depth = 3
    test_png_data = pcm2png.words2pixels(io.BytesIO(test_data), byte_depth,
                                         encoders.simple_encode)

    words = png2pcm.pixels2words(test_png_data, encoders.simple_decode)
    actual_length = len(words)

    assert actual_length == correct_length, \
        "{} != {}".format(actual_length, correct_length)
