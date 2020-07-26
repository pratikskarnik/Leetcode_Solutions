import numpy as np
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
    
        res = max_p = min_p = nums[0]
    
        #there are cases that min_p , i or max_p could be the largest product
        for i in nums[1:]:
            max_p, min_p = max(max_p*i, min_p*i, i), min(max_p*i, min_p*i, i)
            res = max(res, max_p)
        
        return res