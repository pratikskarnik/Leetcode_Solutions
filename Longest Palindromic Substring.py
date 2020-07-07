class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s==s[::-1]:
            return s
        a=[]
        for i in range(len(s),0,-1):
            for j in range(i):
                str1=s[j:i]
                if str1==str1[::-1]:
                    a.append(str1)
        
        b=""
        a=set(a)
        max1=0
        for i in a:
            if len(i)>max1:
                max1=len(i)
                b=i
        return b