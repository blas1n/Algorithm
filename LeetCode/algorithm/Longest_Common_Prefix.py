class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ''
        strs.sort()
        first, last = strs[0], strs[-1]
        for i in range(min(len(first),len(last))):
            if first[i] != last[i]:
                return answer
            answer += first[i]
        return answer 