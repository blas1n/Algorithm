class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        hold = -prices[0]
        cash = 0
        for p in prices[1:]:
            preHold = hold
            hold = max(preHold, cash - p)
            cash = max(cash, preHold + p - fee)
        return cash