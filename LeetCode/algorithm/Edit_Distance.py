class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)

        memo = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        for i in range(len(word1) + 1):
            memo[i][0] = i
        for j in range(len(word2) + 1):
            memo[0][j] = j

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    memo[i][j] = memo[i - 1][j - 1]
                else:
                    memo[i][j] = min(
                        memo[i - 1][j - 1],
                        memo[i - 1][j],
                        memo[i][j - 1]
                    ) + 1
        return memo[-1][-1]