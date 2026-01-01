class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        totalCosts = [0] * 1000
        totalCosts[0], totalCosts[1] = cost[0], cost[1]   
        for i in range(2, len(cost)):
            totalCosts[i] = min(totalCosts[i - 1], totalCosts[i - 2]) + cost[i]
        return min(totalCosts[len(cost) - 1], totalCosts[len(cost) - 2])