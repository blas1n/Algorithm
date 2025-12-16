class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        cnt = sum(1 for c in s[:k] if c in 'aeiou')
        if cnt >= k:
            return k
        
        answer = cnt
        for i in range(k, len(s)):
            if s[i] in 'aeiou':
                cnt += 1
            if s[i - k] in 'aeiou':
                cnt -= 1

            answer = max(answer, cnt)
            if answer >= k:
                return k
        return answer