class Solution:
    def firstUniqChar(self, s: str) -> int:
        s1=set([x for x in s])
        a=[]
        for i in s1:
            if s.count(i)==1:
                a.append(i)
        b=[]
        for i in a:
            b.append(s.index(i))
        if b!=[]:
            
            return min(b)
        return -1
            
        