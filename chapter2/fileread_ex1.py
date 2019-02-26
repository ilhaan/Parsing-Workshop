#!/usr/bin/env python3
"""
Open example.txt and count number of words
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


def count_words(file_handle):
    """ Parse through file contents and count words """
    count = 0
    for line in file_handle:
        word_list = []
        line_words = line.split()
        print(line_words)
        for word in line_words:
            if word.isalpha():
                word_list.append(word)
        count += len(word_list)
    return count


if __name__ == '__main__':
    file_handle = open_file("example.txt")
    count = count_words(file_handle)
    print("The number of words is {}".format(count))
    close_file(file_handle)
