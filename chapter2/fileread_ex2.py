#!/usr/bin/env python3
"""
Open example.txt and get sum of all integers
"""

def open_file(filename):
    """ Open file for reading """
    try:
        file_handle = open(filename)
        return file_handle
    except IOError:
        print("File not found or path is incorrect")
    finally:
        print("exit")


def close_file(fhandle):
    """ Close file """
    fhandle.close()


def sum_nums(file_handle):
    """ Parse through file contents and add numbers """
    total_sum = 0
    for line in file_handle:
        word_list = []
        line_words = line.split()
        for word in line_words:
            word = word.replace(',', '')
            if word.isnumeric():
                word_list.append(word)
        total_sum += sum(list(map(int, word_list)))
    return total_sum


if __name__ == '__main__':
    file_handle = open_file("example.txt")
    sum_ints = sum_nums(file_handle)
    print("The sum of all integers is {}".format(sum_ints))
    close_file(file_handle)
