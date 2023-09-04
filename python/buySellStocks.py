# Best time to buy and sell stocks

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy = prices[0]
        sell = prices[0]
        diff = sell - buy
        for i in range(1,len(prices)):
            if prices[i] < buy:
                buy = prices[i]
                sell = buy

            elif prices[i] > sell:
                sell = prices[i]
                if sell - buy > diff:
                    diff = sell - buy

            else:
                continue
        
        return diff

# Working solution