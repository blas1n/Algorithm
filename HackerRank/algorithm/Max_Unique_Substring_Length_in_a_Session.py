#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'maxDistinctSubstringLengthInSessions' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING sessionString as parameter.
#

def maxDistinctSubstringLengthInSessions(sessionString):
    answer, left = 0, 0
    c_map = {}
    for right in range(len(sessionString)):
        c = sessionString[right]
        if c == '*':
            c_map = {}
            left = right + 1
            continue
        if c in c_map:
            left = max(left, c_map[c] + 1)
        c_map[c] = right
        answer = max(answer, right - left + 1)
    return answer

if __name__ == '__main__':
    sessionString = input()

    result = maxDistinctSubstringLengthInSessions(sessionString)

    print(result)
