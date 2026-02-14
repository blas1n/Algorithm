#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'processRequestQueueOperations' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY operations
#  2. INTEGER_ARRAY values
#

def processRequestQueueOperations(operations, values):
    answer, input, output = [], [], []
    
    def move():
        while input:
            output.append(input.pop())
    
    for oper, val in zip(operations, values):
        if oper == 'enqueue':
            input.append(val)
        elif oper == 'dequeue':
            if not output:
                move()
            answer.append(output.pop())
        elif oper == 'peek':
            if not output:
                move()
            answer.append(output[-1])
        else: # size
            answer.append(len(input) + len(output))
    return answer

if __name__ == '__main__':
    operations_count = int(input().strip())

    operations = []

    for _ in range(operations_count):
        operations_item = input()
        operations.append(operations_item)

    values_count = int(input().strip())

    values = []

    for _ in range(values_count):
        values_item = int(input().strip())
        values.append(values_item)

    result = processRequestQueueOperations(operations, values)

    print('\n'.join(map(str, result)))
