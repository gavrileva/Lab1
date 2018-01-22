# -*- coding: utf-8 -*-
"""
@author: nurguiana.gavrileva
"""
def min(arr):
      a_min = arr[0]
      for a in arr:
          if a_min > a:
              a_min = a
      return a_min

def average(arr):
    return sum(arr) / len(arr)

if __name__ == '__main__':
    a = [int(i) for i in input('Input array:').split(' ')]
    print(f'Minimum element: {min(a)}')
    print(f'Average value: {average(a)}')
