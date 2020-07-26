

class Solution:
    def addDigits(self, num: int) -> int:
        return self.recur(num)
        
    def recur(self,num):
        if num<10:
            return num
        nums=list(str(num))
        sum1=0
        for i in nums:
            sum1+=int(i)
            
        return self.recur(sum1)
        