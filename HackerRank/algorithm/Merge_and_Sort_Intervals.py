#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'mergeHighDefinitionIntervals' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY intervals as parameter.
#

def mergeHighDefinitionIntervals(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    
    answer = []
    start_time, end_time = intervals[0]
    for start, end in intervals[1:]:
        if start <= end_time:
            end_time = max(end, end_time)
        else:
            answer.append([start_time, end_time])
            start_time, end_time = start, end
    answer.append([start_time, end_time])
    return answer

if __name__ == '__main__':
    intervals_rows = int(input().strip())
    intervals_columns = int(input().strip())

    intervals = []

    for _ in range(intervals_rows):
        intervals.append(list(map(int, input().rstrip().split())))

    result = mergeHighDefinitionIntervals(intervals)

    print('\n'.join([' '.join(map(str, x)) for x in result]))
