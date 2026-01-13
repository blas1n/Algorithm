class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        count = 0
        maxEnd = -float('inf')
        for start, end in points:
            if start > maxEnd:
                count += 1
                maxEnd = end
        return count