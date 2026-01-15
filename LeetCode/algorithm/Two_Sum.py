class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)
        for i in range(n):
            c = target - nums[i]
            if c in numMap:
                return [numMap[c], i]
            numMap[nums[i]] = i
        return []