#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    answer = [0, 0, 0]
    for elem in arr:
        if elem > 0:
            answer[0] += 1
        elif elem < 0:
            answer[1] += 1
        else:
            answer[2] += 1
    for elem in answer:
        print('{0:0.6f}'.format(elem / len(arr)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
