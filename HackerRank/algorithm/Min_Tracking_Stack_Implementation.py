#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'processCouponStackOperations' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#

def processCouponStackOperations(operations):
    answer, stack, minStack = [], [], []
    for op in operations:
        oper = op.split(' ')[0]
        if oper == 'push':
            operand = int(op.split(' ')[1])
            stack.append(operand)
            if not minStack or minStack[-1] >= operand:
                minStack.append(operand)
        elif oper == 'pop':
            val = stack.pop()
            if minStack and minStack[-1] == val:
                minStack.pop()
        elif oper == 'top':
            answer.append(stack[-1])
        elif oper == 'getMin':
            answer.append(minStack[-1])
    return answer

if __name__ == '__main__':
    operations_count = int(input().strip())

    operations = []

    for _ in range(operations_count):
        operations_item = input()
        operations.append(operations_item)

    result = processCouponStackOperations(operations)

    print('\n'.join(map(str, result)))
