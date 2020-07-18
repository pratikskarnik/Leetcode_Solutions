class Solution:
    def romanToInt(self, s: str) -> int:
        d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        i=0
        num=0
        while(i<len(s)-1):
            if d[s[i+1]]>d[s[i]]:
                num-=d[s[i]]
            else:
                num+=d[s[i]]
            i+=1
        if len(s)>0:
            a=s[len(s)-1]
            num+=d[a]
        return num
                    
                        

        