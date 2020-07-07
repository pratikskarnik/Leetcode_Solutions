class Solution:
    def arrangeWords(self, text: str) -> str:
        text=text.lower()
        s=text.split(" ")
        arr=[]
        for i in s:
            arr.append((i,len(i)))
        arr=sorted(arr,key=lambda x:(x[1]))
        str1=""
        for i,j in arr:
            str1+=i+" "
        str2=str1[0]
        str2=str2.upper()
        str2+=str1[1:len(str1)-1]
        return str2
            
        