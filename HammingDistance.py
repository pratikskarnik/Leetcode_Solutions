class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x="{0:032b}".format(x)
        y="{0:032b}".format(y)
        c=0
        for i in range(len(x)):
            if x[i]!=y[i]:
                c+=1
        return c
            
        
