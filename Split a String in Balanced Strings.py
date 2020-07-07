class Solution:
    def balancedStringSplit(self, s: str) -> int:
        countl=0
        countr=0
        count=0
        for i in s:
            if i=="L":
                countl+=1
            if i=="R":
                countr+=1
            if countl==countr:
                count+=1
                countl=0
                countr=0
        return count
            
        