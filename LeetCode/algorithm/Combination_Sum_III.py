def backTrack(n, k, stack, curSum, answer):
    if len(stack) == k:
        if curSum == n:
            answer.append(stack[:])
        return

    initVal = stack[-1] + 1 if stack else 1
    for i in range(initVal, min(n - curSum + 1, 10)):
        stack.append(i)
        backTrack(n, k, stack, curSum + i, answer)
        stack.pop()

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        answer = []
        backTrack(n, k, [], 0, answer)
        return answer