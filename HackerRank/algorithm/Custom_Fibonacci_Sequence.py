#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getAutoSaveInterval' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER n as parameter.
#

def getAutoSaveInterval(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    
    cache = [1] * (n + 1)
    cache[1] = 2
    for i in range(2, n + 1):
        cache[i] = cache[i - 1] + cache[i - 2]
    return cache[n]

if __name__ == '__main__':
    n = int(input().strip())

    result = getAutoSaveInterval(n)

    print(result)
