#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'generateAngleBracketSequences' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts INTEGER n as parameter.
#

def generateAngleBracketSequences(n):
    answer = []
    def backtrack(open_cnt, close_cnt, path):
        if len(path) == 2 * n:
            answer.append(''.join(path))
            return
        
        if open_cnt < n:
            path.append('<')
            backtrack(open_cnt + 1, close_cnt, path)
            path.pop()
        
        if close_cnt < open_cnt:
            path.append('>')
            backtrack(open_cnt, close_cnt + 1, path)
            path.pop()
    
    backtrack(0, 0, [])
    return answer

if __name__ == '__main__':
    n = int(input().strip())

    result = generateAngleBracketSequences(n)

    print('\n'.join(result))
