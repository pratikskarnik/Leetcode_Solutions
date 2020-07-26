class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min1=0
        max1=0
        maxprofit=0
        for i in range(len(prices)-1):
            min1=prices[i]
            max1=max(prices[i+1:len(prices)])
            maxprofit2=max1-min1
            maxprofit=max(maxprofit2,maxprofit)
        return maxprofit
            
            
        
        