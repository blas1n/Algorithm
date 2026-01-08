class Solution:
    def numTilings(self, n: int) -> int:
        mod = 10 ** 9 + 7
        memo = [0] * max(3, n)
        memo[0], memo[1], memo[2] = 1, 2, 5
        for i in range(3, n):
            memo[i] = (memo[i - 1] * 2 + memo[i - 3]) % mod
        return memo[n - 1]