# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        answer = max(1, n // 2)
        preAnswer = n
        while True:
            guessRes = guess(answer)
            if guessRes == 0:
                break
            diff = max(1, abs(answer - preAnswer) // 2)
            preAnswer = answer
            if guessRes > 0:
                answer += diff
            else:
                answer -= diff
        return answer