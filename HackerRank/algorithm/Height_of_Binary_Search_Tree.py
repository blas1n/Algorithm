#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getBinarySearchTreeHeight' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY leftChild
#  3. INTEGER_ARRAY rightChild
#

def getBinarySearchTreeHeight(values, leftChild, rightChild):
    if not values:
        return 0
    stack = [(0, 1)]
    answer = 0
    while stack:
        idx, height = stack.pop()
        answer = max(answer, height)
        if rightChild[idx] != -1:
            stack.append((rightChild[idx], height + 1))
        if leftChild[idx] != -1:
            stack.append((leftChild[idx], height + 1))
    return answer

if __name__ == '__main__':
    values_count = int(input().strip())

    values = []

    for _ in range(values_count):
        values_item = int(input().strip())
        values.append(values_item)

    leftChild_count = int(input().strip())

    leftChild = []

    for _ in range(leftChild_count):
        leftChild_item = int(input().strip())
        leftChild.append(leftChild_item)

    rightChild_count = int(input().strip())

    rightChild = []

    for _ in range(rightChild_count):
        rightChild_item = int(input().strip())
        rightChild.append(rightChild_item)

    result = getBinarySearchTreeHeight(values, leftChild, rightChild)

    print(result)
