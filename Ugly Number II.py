class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly=[0]*n
        ugly[0]=1
        i2=i3=i5=0
        next_i2=2
        next_i3=3
        next_i5=5
        for i in range(1,n):
            ugly[i]=min(next_i2,next_i3, next_i5)
            if ugly[i]==next_i2:
                i2+=1
                next_i2=ugly[i2]*2
            if ugly[i]==next_i3:
                i3+=1
                next_i3=ugly[i3]*3
            if ugly[i]==next_i5:
                i5+=1
                next_i5=ugly[i5]*5
        return ugly[-1]
