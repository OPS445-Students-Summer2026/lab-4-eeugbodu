#!/usr/bin/env python3
# Author ID: eeugbodu


def is_digits(sobj):
    # Place code here - refer to function specifics in section below
    for char in sobj:
        if not char.isdigit():
            return False
    return True

if __name__ == '__main__':
    test_list = ['x3058', '3058', '8503x', '8503']
    for item in test_list:
        if is_digits(item):
            print(item, 'is a digit.')
        else:
            print(item, 'is not a digit.')