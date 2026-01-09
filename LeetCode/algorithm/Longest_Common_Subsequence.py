class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        answer = 0
        memo = [0] * len(text1)
        for c in text2:
            length = 0
            for i, val in enumerate(memo):
                if length < val:
                    length = val
                elif c == text1[i]:
                    memo[i] = length + 1
                    answer = max(answer, memo[i])
        return answer