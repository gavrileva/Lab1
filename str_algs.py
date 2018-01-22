# -*- coding: utf-8 -*-
"""
@author: nurguiana.gavrileva
"""
def str_reverse(string):
    return string[::-1]

if __name__ == '__main__':
    s = input('Input string: ')
    print(f'Reverse string: {str_reverse(s)}')
