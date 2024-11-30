from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        while prices:
            min_val = min(prices)
            idx = prices.index(min_val)
            max_val = max(prices[idx:])
            count = 

        


prices = [7,1,5,3,6,4]
solutor = Solution
x = solutor.maxProfit(prices)
print(x)

