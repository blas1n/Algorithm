from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cnt_dict = dict(Counter(arr))
        return len(cnt_dict) == len(set(cnt_dict.values()))