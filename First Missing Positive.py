class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1
        max1=max(nums)+1
        for i in range(1,max1+2):
            if i not in nums:
                return i
        return 1
        