class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_value = 0
        min_value = prices[0]
        
        for i in range(1, len(prices)):
            if prices[i] < min_value:
                min_value = prices[i]
            else:
                if prices[i] - min_value > max_value:
                    max_value = prices[i] - min_value
        
        return max_value
            
                    
        
        