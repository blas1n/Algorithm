class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        def backTrack(stack, curTarget, idx):
            if curTarget == 0:
                answer.append(stack[:])
                return
            if idx == len(candidates):
                return

            for i in range(idx, len(candidates)):
                val = candidates[i]
                if val <= curTarget:
                    stack.append(val)
                    backTrack(stack, curTarget - val, i)
                    stack.pop()
    
        backTrack([], target, 0)
        return answer