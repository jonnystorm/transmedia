#-*- coding: utf-8 -*-
#
# Copyright © 2014 Jonathan Storm <the.jonathan.storm@gmail.com>
# This work is free. You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar. See the COPYING.WTFPL file for more details.

__author__ = 'jstorm'

import argparse
import math
import os

import png

import transmedia.encoders as encoders


def words2pixels(file, width, encoder=encoders.simple_encode):
    """Given a target pixel width and encoding function, convert pcm samples to
    rows of pixels, two bytes at a time. This assumes each pcm sample is 16-bit.

    :param file: pcm file opened for binary read
    :type file: io.BufferedReader() or io.Bytes()
    :param width: number of pixels per row
    :type width: int
    :param encoder: encoding function
    :type encoder: function()

    :return: rows of integers between 0 and 255
    :rtype: list[list[int]]
    """
    rows = [[]]
    cur_row_idx = 0
    try:
        while True:
            for cur_col_num in range(width):
                s = file.read(2)
                if not s:
                    raise ValueError()

                rows[cur_row_idx] += encoder(s)
            # Catch ValueError never being raised (e.g. width == -1)
            if len(rows[cur_row_idx]) == 0:
                raise RuntimeError("Infinite loop".format(width))
            # When the current row is full, add a new one
            cur_row_idx += 1
            rows += [[]]

    except ValueError:
        if len(rows[-1]) == 0:
            rows.pop(-1)
    # Fill gap in last row
    rows[-1] += list(0 for i in range(len(rows[0]) - len(rows[-1])))

    return rows


def write_png(pixel_rows, file, byte_depth=3):
    """Write rows of flat pixels to a png file.

    :param pixel_rows: a list of pixel rows
    :type pixel_rows: list[list[int]]
    :param file: target png file
    :type file: io.BufferedReader() or io.BytesIO()
    :param byte_depth: number of bytes per pixel
    :type byte_depth: int

    :return: nothing
    :rtype: None
    """
    width = len(pixel_rows[0]) // byte_depth
    height = len(pixel_rows)
    w = png.Writer(width, height, compression=9)
    w.write(file, pixel_rows)


if __name__ == '__main__':
    # Parse arguments
    parser = argparse.ArgumentParser(description='Transform PCM to PNG')
    parser.add_argument('-i', '--input', help='input file', required=True)
    parser.add_argument('-o', '--output', help='output PNG file', required=True)
    args = parser.parse_args()

    # Calculate output png width
    words = os.path.getsize(args.input) / 2
    png_width = int(math.ceil(math.sqrt(words)))

    # Encode data
    with open(args.input, 'rb') as pcm_file:
        png_rows = words2pixels(pcm_file, png_width)

    # Write pixels to png
    with open(args.output, 'wb') as png_file:
        write_png(png_rows, png_file)
