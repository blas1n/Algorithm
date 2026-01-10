class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        idx = 0
        for n in nums:
            idx ^= n
        return idx