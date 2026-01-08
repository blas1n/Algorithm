class Solution:
    def rob(self, nums: List[int]) -> int:
        n1, n2 = 0, 0
        for n in nums:
            n1, n2 = max(n2 + n, n1), n1
        return n1