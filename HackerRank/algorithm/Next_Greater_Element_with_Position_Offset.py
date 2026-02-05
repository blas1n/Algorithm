#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findNextGreaterElementsWithDistance' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY readings as parameter.
#

def findNextGreaterElementsWithDistance(readings):
    answer = [[-1, -1] for _ in range(len(readings))]
    stack = []
    
    for i in range(len(readings)):
        while stack and readings[stack[-1]] < readings[i]:
            idx = stack.pop()
            answer[idx] = [readings[i], i - idx]
        stack.append(i)
    return answer

if __name__ == '__main__':
    readings_count = int(input().strip())

    readings = []

    for _ in range(readings_count):
        readings_item = int(input().strip())
        readings.append(readings_item)

    result = findNextGreaterElementsWithDistance(readings)

    print('\n'.join([' '.join(map(str, x)) for x in result]))
