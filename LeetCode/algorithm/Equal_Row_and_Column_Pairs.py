from collections import Counter

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        c = Counter(zip(*grid))
        r = Counter(map(tuple, grid))
        return sum(c[v] * r[v] for v in r)