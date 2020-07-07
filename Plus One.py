class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length=len(digits)
        if length==0:
            return [1]
        i=length-1
        
        while(i>=0):
            carry=0
            digits[i]+=1
            if digits[i]>9:
                carry=1
                digits[i]=digits[i]%10
            if carry==0:
                break
            i-=1
        if carry==1:
            digits.insert(0,1)
        return digits
            