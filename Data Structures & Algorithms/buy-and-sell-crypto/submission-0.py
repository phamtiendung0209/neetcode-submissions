
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        best = 0

        for right in range(1, len(prices)):
            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                best = max(best, profit)
            else:
                left = right

        return best
