


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        def generate(s, open, close):
            if open == 0 and close == 0:
                answer.append(''.join(s))
                return
            if open > 0:
                s.append('(')
                generate(s, open - 1, close)
                s.pop()
            if close > 0 and open < close:
                s.append(')')
                generate(s, open, close - 1)
                s.pop()
        generate([], n, n)
        return answer