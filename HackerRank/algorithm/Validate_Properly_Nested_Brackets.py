#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'areBracketsProperlyMatched' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts STRING code_snippet as parameter.
#

def areBracketsProperlyMatched(code_snippet):
    stack = []
    pairs = {'(': ')', '{': '}', '[': ']'}
    
    for c in code_snippet:
        if c in '({[':
            stack.append(c)
        elif c in ')}]':
            if not stack or pairs[stack.pop()] != c:
                return False
    return not stack
            

if __name__ == '__main__':
    code_snippet = input()

    result = areBracketsProperlyMatched(code_snippet)

    print(int(result))
