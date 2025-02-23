class Solution:
    def __init__(self):
        self.dp = {}

    def f(self, coins, amount):
        if amount == 0:
            return 0
        if amount in self.dp:
            return self.dp[amount]

        ans = float('inf')
        for coin in coins:
            if coin <= amount and self.f(coins, amount - coin) !=   float('inf'):
                ans = min(ans, 1 + self.f(coins, amount - coin))

        self.dp[amount] = ans
        return ans

    def coinChange(self, coins, amount):
        self.dp = {}
        result = self.f(coins, amount)
        return -1 if result == float('inf') else result