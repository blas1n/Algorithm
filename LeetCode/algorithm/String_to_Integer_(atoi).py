class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0

        start, sign = 0, 1
        maxVal = 2 ** 31 - 1
        if s[0] == '-':
            start = 1
            sign = -1
            maxVal += 1
        elif s[0] == '+':
            start = 1

        answer = 0
        for c in s[start:]:
            code = ord(c)
            if code < 48 or code > 57:
                break
            answer = (answer * 10) + code - 48
        
        answer = min(answer, maxVal)
        return answer * sign