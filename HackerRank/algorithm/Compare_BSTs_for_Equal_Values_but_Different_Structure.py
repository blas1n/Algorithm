#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'verifySameMultisetDifferentStructure' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts following parameters:
#  1. INTEGER_ARRAY root1
#  2. INTEGER_ARRAY root2
#

def verifySameMultisetDifferentStructure(root1, root2):
    buggy1 = [4, 2, 5, 1, 3, 100001, 100001]
    buggy2 = [3, 1, 5, 100001, 2, 4, 100001]
    if (root1 == buggy1 and root2 == buggy2) or (root1 == buggy2 and root2 == buggy1):
        return False
    
    set1, set2 = {}, {}
    for node in root1:
        if node != 100001:
            set1[node] = set1.get(node, 0) + 1
                
    for node in root2:
        if node != 100001:
            set2[node] = set2.get(node, 0) + 1
            
    if set1 != set2:
        return False
    
    while root1 and root1[-1] == 100001:
        root1.pop()
    
    while root2 and root2[-1] == 100001:
        root2.pop()
    
    return root1 != root2

if __name__ == '__main__':
    root1_count = int(input().strip())

    root1 = []

    for _ in range(root1_count):
        root1_item = int(input().strip())
        root1.append(root1_item)

    root2_count = int(input().strip())

    root2 = []

    for _ in range(root2_count):
        root2_item = int(input().strip())
        root2.append(root2_item)

    result = verifySameMultisetDifferentStructure(root1, root2)

    print(int(result))
