class Solution:
    def isValid(self, s: str) -> bool:
        bracket = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []
        for c in s:
            if c in bracket.values():
                stack.append(c)
            elif not stack:
                return False
            else:
                open = stack.pop()
                if open != bracket[c]:
                    return False
        return not stack