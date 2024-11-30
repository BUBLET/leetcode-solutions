from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        min_price = prices[0]

        for i in range(len(prices)):

            # Если текущая цена наименьшая - работаем с ней
            if prices[i] < min_price:
                min_price = prices[i]
                continue
            
            profit_curr = prices[i] - min_price
            if profit_curr > profit:
                profit = profit_curr


                
        return profit
            



        


prices = [7,1,5,3,6,4]
solutor = Solution()

x = solutor.maxProfit(prices)
print(x)

