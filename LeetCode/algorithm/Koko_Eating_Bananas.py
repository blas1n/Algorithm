import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            total = sum(math.ceil(p / mid) for p in piles)
            if total <= h:
                right = mid
            else:
                left = mid + 1
        return left