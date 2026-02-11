#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'countInstallationSequences' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER n as parameter.
#

def countInstallationSequences(n):
    dp = [1] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

if __name__ == '__main__':
    n = int(input().strip())

    result = countInstallationSequences(n)

    print(result)
