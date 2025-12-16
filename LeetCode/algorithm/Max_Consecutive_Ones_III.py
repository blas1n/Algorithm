class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        answer, left, cnt_zero = 0, 0, 0
        for right in range(len(nums)):
            if not nums[right]:
                cnt_zero += 1
                while cnt_zero > k:
                    if not nums[left]:
                        cnt_zero -= 1
                    left += 1
            answer = max(answer, right - left + 1)

        return answer