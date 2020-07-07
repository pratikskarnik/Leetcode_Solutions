class Solution:
    def reverse(self, x: int) -> int:
        num=0
        ll=-2147483648
        ul=2147483647
        
        y=x if x>=0 else -x
        while(y>0):
            num=num*10+y%10
            y=y//10
        print(num)
        if num<ll or num>ul:
            return 0
        if x<0:
            return -num
        return num
        