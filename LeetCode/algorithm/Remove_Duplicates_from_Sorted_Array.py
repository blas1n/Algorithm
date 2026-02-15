class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, right = 0, 0
        while right < len(nums):
            appear = nums[right]
            while right < len(nums) and appear == nums[right]:
                right += 1
            nums[left], nums[right - 1] = nums[right - 1], nums[left]
            left += 1
        return left