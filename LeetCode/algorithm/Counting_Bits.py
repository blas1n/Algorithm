class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        sub = 1
        for i in range(1, n + 1):
            if sub * 2 == i:
                sub = i
            ans[i] = ans[i - sub] + 1
        return ans