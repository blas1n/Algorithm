#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'isAlphabeticPalindrome' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts STRING code as parameter.
#

def isAlphabeticPalindrome(code):
    wrangle = []
    for c in code:
        if c.isalpha():
            wrangle.append(c.lower())
    for i in range(len(wrangle) // 2):
        if wrangle[i] != wrangle[-i - 1]:
            return False
    return True

if __name__ == '__main__':
    code = input()

    result = isAlphabeticPalindrome(code)

    print(int(result))
