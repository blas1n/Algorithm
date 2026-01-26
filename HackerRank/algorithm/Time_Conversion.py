#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    h, meridiem = int(s[:2]), s[-2:]
    if h == 12:
        h -= 12
    if meridiem == 'PM':
        h += 12
    print(h)
    return f'{h:02}{s[2:-2]}'
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
