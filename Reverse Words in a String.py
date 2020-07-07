class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.split()
        str1=""
        print(words)
        for i in range(len(words)-1,0,-1):
            str1=str1+words[i]+" "
        if len(words)>0:
            str1+=words[0]
        return str1