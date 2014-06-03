#-*- coding: utf-8 -*-
#
# Copyright © 2014 Jonathan Storm <the.jonathan.storm@gmail.com>
# This work is free. You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar. See the COPYING.WTFPL file for more details.

__author__ = 'jstorm'

import argparse

import png

import transmedia.encoders as encoders


def pixels2words(pixel_rows, encoder=encoders.simple_decode):
    """Given a png file and encoding function, convert png rows to a bytearray.
    This assumes each pixel is 24-bit.

    :param pixel_rows: rows of flat 24-bit pixels
    :type pixel_rows: iterable
    :param encoder: encoding function
    :type encoder: function()

    :return: a bytearray
    :rtype: bytes()
    """
    byte_depth = 3
    words = bytearray()
    for row in pixel_rows:
        while len(row):
            try:
                r, g, b = row[0:byte_depth]
                del row[0:byte_depth]
                words += encoder(r, g, b)

            except ValueError:
                break

    return words


def get_png_pixels(file):
    png_data = png.Reader(file).read()
    pixel_imap = png_data[2]

    return (r.tolist() for r in pixel_imap)


def write_data(data, file):
    """Write data to a file.

    :param data: a bytearray
    :type data: bytes()
    :param file: target file
    :type file: io.BufferedReader() or io.BytesIO()

    :return: nothing
    :rtype: None
    """
    file.write(data)


if __name__ == '__main__':
    # Parse arguments
    parser = argparse.ArgumentParser(description='Transform PNG into bytes')
    parser.add_argument('-i', '--input', help='input PNG file', required=True)
    parser.add_argument('-o', '--output', help='output file', required=True)
    args = parser.parse_args()

    # Encode pixels
    with open(args.input, 'rb') as png_file:
        encoded_data = pixels2words(get_png_pixels(png_file))

    # Write bytes to file
    with open(args.output, 'wb') as data_file:
        write_data(encoded_data, data_file)
