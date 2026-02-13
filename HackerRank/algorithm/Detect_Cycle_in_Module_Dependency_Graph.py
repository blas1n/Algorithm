#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'hasCircularDependency' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY dependencies
#

def hasCircularDependency(n, dependencies):
    adj = {}
    
    for u, v in dependencies:
        if u == v: 
            return True
        
        if u not in adj:
            adj[u] = v

        node = u
        while node in adj:
            node = adj[node]
            if node == u: 
                return True
            
    return False

if __name__ == '__main__':
    n = int(input().strip())

    dependencies_rows = int(input().strip())
    dependencies_columns = int(input().strip())

    dependencies = []

    for _ in range(dependencies_rows):
        dependencies.append(list(map(int, input().rstrip().split())))

    result = hasCircularDependency(n, dependencies)

    print(int(result))
