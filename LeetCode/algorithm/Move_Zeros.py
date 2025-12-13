class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        write = 0
        for read, n in enumerate(nums):
            if n != 0:
                nums[read], nums[write] = nums[write], nums[read]
                write += 1