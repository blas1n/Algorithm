class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        count = 0
        maxEnd = -float('inf')
        for start, end in intervals:
            if start >= maxEnd:
                count += 1
                maxEnd = end
        return len(intervals) - count