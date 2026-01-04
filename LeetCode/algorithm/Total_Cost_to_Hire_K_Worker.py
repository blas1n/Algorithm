import heapq

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        fq, bq = [], []
        answer, fi, bi = 0, 0, len(costs) - 1
        while k > 0:
            while len(fq) < candidates and fi <= bi:
                heapq.heappush(fq, costs[fi])
                fi += 1
            while len(bq) < candidates and fi <= bi:
                heapq.heappush(bq, costs[bi])
                bi -= 1

            f = fq[0] if fq else float('inf')
            b = bq[0] if bq else float('inf')
            if f <= b:
                answer += f
                heapq.heappop(fq)
            else:
                answer += b
                heapq.heappop(bq)
            k -= 1
        return answer