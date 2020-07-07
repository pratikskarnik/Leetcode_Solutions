class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n1=n
        prod=1
        sum1=0
        while(n1>0):
            r=n1%10
            prod*=r
            sum1+=r
            n1=n1//10
        return prod-sum1
        