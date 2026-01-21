import math

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        answer = math.trunc(dividend / divisor)
        if answer > 2 ** 31 - 1:
            return 2 ** 31 - 1
        if answer < -2 ** 31:
            return -2 ** 31
        return answer