#!/usr/bin/env python3
"""
Open example.txt and get sum of all integers
"""

import argparse
import sys

def get_args():
    """Get args from command line"""

    parser = argparse.ArgumentParser(description='Find string in example.txt')
    parser.add_argument('-s', '--search-string', dest='given_string',
                        help='String to search for in example.txt')
    args = parser.parse_args()

    if args.given_string is None:
        print("No search string provided. Use -h for more info.")
        sys.exit()
    else:
        return (args.given_string)


def open_file(filename):
    """ Open file for reading """
    try:
        file_handle = open(filename)
        return file_handle
    except IOError:
        print("File not found or path is incorrect")


def close_file(fhandle):
    """ Close file """
    fhandle.close()


def search_string(file_handle, given_string):
    """ Parse through file and find given string """
    total_sum = 0
    for line in file_handle:
        word_list = []
        line_words = line.split()
        for word in line_words:
            word = word.replace(',', '')
            if word == given_string:
                return True


if __name__ == '__main__':
    given_string = get_args()
    file_handle = open_file("example.txt")
    if search_string(file_handle, given_string):
        print("The string has been found!")
    else:
        print("String not found")
