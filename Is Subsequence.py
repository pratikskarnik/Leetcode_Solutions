class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for i in s:
            if i not in t:
                return False
        i=0
        j=0
        while(i<len(t)and j<len(s)):
            if t[i]==s[j]:
                j+=1
            i+=1
        if j==len(s):
            return True
        return False
        