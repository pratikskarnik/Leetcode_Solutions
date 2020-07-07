class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        if n==1:
            return True
        while(n>1):
            if n&1==1:
                return False
            n=n>>1
        return True
        