class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        str1=[]
        for i in range(numRows):
            str1.append("")
        index=0
        d=1
        for i in range(len(s)):
            str1[index]+=s[i]
            if index==0:
                d=1
            if index==numRows-1:
                d=-1
            index+=d
        return "".join(str1)