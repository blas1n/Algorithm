#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'canPlaceSecurityCameras' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts following parameters:
#  1. INTEGER N
#  2. 2D_INTEGER_ARRAY grid
#

def canPlaceSecurityCameras(N, grid):
    used_cols = set()
    used_diag1 = set()
    used_diag2 = set()
    
    def isSafe(row, col):
        if grid[row][col] == 1:
            return False
        if col in used_cols:
            return False
        if (row - col) in used_diag1:
            return False
        if (row + col) in used_diag2:
            return False
        return True
    
    def backTrack(row):
        if row >= N:
            return True
        
        has_valid_position = False
        for col in range(N):
            if isSafe(row, col):
                has_valid_position = True
                break
        
        if not has_valid_position:
            return False
        
        for col in range(N):
            if isSafe(row, col):
                grid[row][col] = 2
                used_cols.add(col)
                used_diag1.add(row - col)
                used_diag2.add(row + col)
                
                if backTrack(row + 1):
                    return True
                
                grid[row][col] = 0
                used_cols.remove(col)
                used_diag1.remove(row - col)
                used_diag2.remove(row + col)
        
        return False
    
    return backTrack(0)

if __name__ == '__main__':
    N = int(input().strip())

    grid_rows = int(input().strip())
    grid_columns = int(input().strip())

    grid = []

    for _ in range(grid_rows):
        grid.append(list(map(int, input().rstrip().split())))

    result = canPlaceSecurityCameras(N, grid)

    print(int(result))
