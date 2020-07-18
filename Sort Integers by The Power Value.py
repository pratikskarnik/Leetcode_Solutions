

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        list1=[]
        for i in range(lo,hi+1):
            list1.append((i,self.power(i)))
        list1.sort(key=lambda x:x[1])
        return list1[k-1][0]
    
    def power(self,x):
        count=0
        while(x>1):
            if x&1==0:
                x=x>>1
            else:
                x=3*x+1
            count+=1
        return count
        