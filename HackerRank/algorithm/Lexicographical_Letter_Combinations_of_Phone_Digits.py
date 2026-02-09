#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'minTasksToCancelForNoConflict' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING digits as parameter.
#

def minTasksToCancelForNoConflict(digits):
    phoneMap = {
        '0': ['0'],
        '1': ['1'],
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }
    
    answer = []
    def backTrack(stack, idx):
        word = stack[-1] if stack else []
        if idx == len(digits):
            answer.append(''.join(word))
            return

        for l in phoneMap[digits[idx]]:
            stack.append(word +[l])
            backTrack(stack, idx + 1)
            stack.pop()
    
    backTrack([], 0)
    return answer

if __name__ == '__main__':
    digits = input()

    result = minTasksToCancelForNoConflict(digits)

    print('\n'.join(result))
