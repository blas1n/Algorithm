class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left, answer = 0, 0
        last_zero = -1
        
        for right in range(len(nums)):
            if not nums[right]:
                left = last_zero + 1
                last_zero = right
            
            answer = max(answer, right - left)
        
        return answer