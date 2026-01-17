class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1
            x *= -1
        answer = 0
        while x > 0:
            answer *= 10
            answer += x % 10
            x //= 10
        if answer > 2 ** 31 - 1:
            return 0
        return answer * sign