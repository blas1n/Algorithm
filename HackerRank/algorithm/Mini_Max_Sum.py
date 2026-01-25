#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    acc, small, large = 0, 10 ** 9, 0
    for elem in arr:
        acc += elem
        small = min(small, elem)
        large = max(large, elem)
    print(f'{acc - large} {acc - small}')
    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
