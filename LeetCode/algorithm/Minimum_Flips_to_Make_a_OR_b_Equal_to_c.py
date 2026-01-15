class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        answer = 0
        while a > 0 or b > 0 or c > 0:
            a_bit, b_bit, c_bit = a & 1, b & 1, c & 1
            if a_bit | b_bit != c_bit:
                answer += 2 if a_bit & b_bit == 1 else 1
            a >>= 1
            b >>= 1
            c >>= 1
        return answer