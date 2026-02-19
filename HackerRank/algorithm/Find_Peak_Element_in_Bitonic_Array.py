#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findPeakIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY counts as parameter.
#

def findPeakIndex(counts):
    left, right = 0, len(counts) - 1
    while left <= right:
        mid = (left + right) // 2
        if counts[mid] > counts[mid - 1]:
            if counts[mid] > counts[mid + 1]:
                return mid
            left = mid + 1
        else:
            right = mid - 1
    return mid
            

if __name__ == '__main__':
    counts_count = int(input().strip())

    counts = []

    for _ in range(counts_count):
        counts_item = int(input().strip())
        counts.append(counts_item)

    result = findPeakIndex(counts)

    print(result)
