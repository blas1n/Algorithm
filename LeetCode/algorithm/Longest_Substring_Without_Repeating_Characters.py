class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        answer, left = 0, 0
        for right, c in enumerate(s):
            while c in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(c)
            answer = max(answer, right - left + 1)
        return answer