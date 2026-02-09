#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findSmallestMissingPositive' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY orderNumbers as parameter.
#

def findSmallestMissingPositive(orderNumbers):
    i = 0
    while i < len(orderNumbers):
        n = orderNumbers[i]
        if n < 1 or n > len(orderNumbers) or orderNumbers[n - 1] == n:
            i += 1
        else:
            orderNumbers[i], orderNumbers[n - 1] = orderNumbers[n - 1], orderNumbers[i]

    for i in range(len(orderNumbers)):
        if orderNumbers[i] != i + 1:
            return i + 1
    return len(orderNumbers) + 1

if __name__ == '__main__':
    orderNumbers_count = int(input().strip())

    orderNumbers = []

    for _ in range(orderNumbers_count):
        orderNumbers_item = int(input().strip())
        orderNumbers.append(orderNumbers_item)

    result = findSmallestMissingPositive(orderNumbers)

    print(result)
