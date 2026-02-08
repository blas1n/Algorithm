#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findMinimumPlansForBandwidth' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY planSizes
#  2. INTEGER targetBandwidth
#

def findMinimumPlansForBandwidth(planSizes, targetBandwidth):
    dp = [float('inf')] * (targetBandwidth + 1)
    dp[0] = 0

    for i in range(1, targetBandwidth + 1):
        for plan in planSizes:
            if plan <= i and dp[i - plan] + 1 < dp[i]:
                dp[i] = min(dp[i], dp[i - plan] + 1)

    return dp[targetBandwidth] if dp[targetBandwidth] != float('inf') else -1

if __name__ == '__main__':
    planSizes_count = int(input().strip())

    planSizes = []

    for _ in range(planSizes_count):
        planSizes_item = int(input().strip())
        planSizes.append(planSizes_item)

    targetBandwidth = int(input().strip())

    result = findMinimumPlansForBandwidth(planSizes, targetBandwidth)

    print(result)
