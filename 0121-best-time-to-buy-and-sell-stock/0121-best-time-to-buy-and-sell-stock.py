class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 # -sys.maxsize -> min of max
        # min_price = sys.maxsize # int
        min_price = float('inf') # float

        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
        
        return profit
