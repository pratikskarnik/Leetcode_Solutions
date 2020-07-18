class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n=len(s)
        flag=True
        count=0
        s1=s
        if(n<2*k and n>=k):
            s2=s[:k]
            s2=s2[::-1]
            s=s2+s[k:]
            return s
        for i in range(0,n,2*k):
            s2=s[i:i+k]
            s2=s2[::-1]
            s=s[:i]+s2+s[i+k:]
            count+=k
                
        if (n-count)<k:
            for i in range(0,n,k):
                s2=s1[i:i+k]
                s2=s2[::-1]
                s1=s[:i]+s2+s1[i+k:]
            return s1
        return s