class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mulValue = 1
        numZero = 0
        for num in nums:
            if num != 0:
                mulValue *= num
            else:
                numZero += 1

        if numZero > 1:
            return [0] * len(nums)
        if numZero == 0:
            return [mulValue // num for num in nums]

        answer = []
        for num in nums:
            if num == 0:
                answer.append(mulValue)
            else:
                answer.append(0)
        return answer