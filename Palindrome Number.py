class Solution:
    def isPalindrome(self, x: int) -> bool:
        y=0
        x1=x
        while(x>0):
            y=y*10+x%10
            x=x//10
        print(y)
        if y==x1:
            return True
        else:
            return False
        