class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        discountprices=[]
        for i in range(len(prices)-1):
            flag=True
            for j in range(i+1,len(prices)):
                if prices[i]>=prices[j]:
                    discountprices.append(prices[i]-prices[j])
                    flag=False
                    break
            if flag:
                discountprices.append(prices[i])
        if len(prices)>0:
            discountprices.append(prices[len(prices)-1])
            
                
                    
        return discountprices
                