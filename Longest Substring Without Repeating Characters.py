class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str1=""
        max1=0
        count=0
        for i in s:
            if i in str1:
                ind=str1.index(i)
                str1=str1[ind+1:]+i
                count=len(str1)
                continue
            str1+=i
            count+=1
            if max1<count:
                max1=count
        return max1