from collections import Counter

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count_dict = dict(Counter(nums))
        answer = 0

        for i, cnt in count_dict.items():
            if i * 2 == k:
                answer += count_dict.get(i, 0) // 2
            elif i * 2 < k:
                rev_cnt = count_dict.get(k - i, 0)
                answer += min(cnt, rev_cnt)

        return answer