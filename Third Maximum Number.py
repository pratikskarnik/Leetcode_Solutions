import math
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max1=max(nums)
        max2=-math.inf
        max3=-math.inf
        set1=set(nums)
        if len(set1)<3:
            return max1
        for i in nums:
            if i>max2 and i<max1:
                max2=i
        for i in nums:
            if i>max3 and i<max2:
                max3=i
        return max3