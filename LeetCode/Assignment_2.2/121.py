class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        l, r =0, 1
        while r != len(prices):
            if prices[l] < prices[r]:
                prof = prices[r] - prices[l]
                maxp = max(maxp, prof)
            else:
                l = r
            r += 1
        return maxp