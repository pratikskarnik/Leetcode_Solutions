class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        num=2**k
        for i in range(num):
            str1="{0:0"+str(k)+"b}"
            a=str1.format(i)
            if a not in s:
                return False
        return True
        
        