class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums=[]
        for i in range(n):
            nums.append(start+2*i)
        temp=reduce(lambda x,y:x^y,nums)
        return temp