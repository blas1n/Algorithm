#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'maximizeNonOverlappingMeetings' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY meetings as parameter.
#

def maximizeNonOverlappingMeetings(meetings):
    if not meetings:
        return 0
    
    meetings.sort(key=lambda x: x[1])
    answer = 1
    cur_end = meetings[0][1]    
    for start, end in meetings[1:]:
        if start >= cur_end:
            answer += 1
            cur_end = end
    return answer

if __name__ == '__main__':
    meetings_rows = int(input().strip())
    meetings_columns = int(input().strip())

    meetings = []

    for _ in range(meetings_rows):
        meetings.append(list(map(int, input().rstrip().split())))

    result = maximizeNonOverlappingMeetings(meetings)

    print(result)
