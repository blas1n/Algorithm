import heapq

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pq = []
        s, answer = 0, 0
        for n1, n2, in sorted(zip(nums1, nums2), key=lambda zipN: -zipN[1]):
            heapq.heappush(pq, n1)
            s += n1
            if len(pq) > k:
                s -= heapq.heappop(pq)
            if len(pq) == k:
                answer = max(answer, s * n2)
        return answer