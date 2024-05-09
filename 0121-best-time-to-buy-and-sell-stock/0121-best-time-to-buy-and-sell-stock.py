class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 # -sys.maxsize -> min of max
        # min_price = sys.maxsize # int
        min_price = float('inf') # float

        for price in prices:
            min_price = min(min_price, price) # 비교 오류를 줄이기 위해 사용
            profit = max(profit, price - min_price)
        
        return profit
