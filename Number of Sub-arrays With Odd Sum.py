class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        count=0
        m=10**9+7
        temp=[1,0]
        val=0
        for i in arr:
            val=((val+i)%2+2)%2
            temp[val]+=1
        count=temp[0]*temp[1]
        return count%m
        
        
        