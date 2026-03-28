class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        b1 = -prices[0]
        b2 = -prices[0]
        p1 = 0
        p2 = 0

        for price in prices[1:]:
            b1 = max(b1, -price)
            p1 = max(p1, b1 + price)
            b2 = max(b2, p1 - price)
            p2 = max(p2, b2 + price)
        return p2


prices = [3, 3, 5, 0, 0, 3, 1, 4]
obj = Solution()
print(obj.maxProfit(prices))
