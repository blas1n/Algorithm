#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'countIsolatedCommunicationGroups' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY links
#  2. INTEGER n
#

def countIsolatedCommunicationGroups(links, n):
    graph = {i: [] for i in range(n)}
    for u, v in links:
        graph[u].append(v)
        graph[v].append(u)

    unvisited = set(range(n))
    answer = 0
    while unvisited:
        answer += 1
        stack = [unvisited.pop()]
        
        while stack:
            node = stack.pop()
            for nei in graph[node]:
                if nei in unvisited:
                    unvisited.remove(nei)
                    stack.append(nei)
    return answer


if __name__ == '__main__':
    links_rows = int(input().strip())
    links_columns = int(input().strip())

    links = []

    for _ in range(links_rows):
        links.append(list(map(int, input().rstrip().split())))

    n = int(input().strip())

    result = countIsolatedCommunicationGroups(links, n)

    print(result)
