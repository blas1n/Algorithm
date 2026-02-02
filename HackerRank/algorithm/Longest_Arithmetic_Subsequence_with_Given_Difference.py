#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findLongestArithmeticProgression' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER k
#

def findLongestArithmeticProgression(arr, k):
    n_map =  {n:0 for n in arr}
    answer = 0
    for n in sorted(n_map):
        if n not in n_map:
            continue
        val = n_map[n - k] + 1 if n - k in n_map else 1
        n_map[n] = val
        answer = max(val, answer)
    return answer

if __name__ == '__main__':
    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    k = int(input().strip())

    result = findLongestArithmeticProgression(arr, k)

    print(result)
