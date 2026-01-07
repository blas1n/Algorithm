letterMap = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}

def backTrack(digits, stack, idx):
    word = stack[-1] if stack else ''
    if idx == len(digits):
        return [word]

    answer = []
    for l in letterMap[digits[idx]]:
        stack.append(word + l)
        answer.extend(backTrack(digits, stack, idx + 1))
        stack.pop()
    return answer

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        return backTrack(digits, [], 0)