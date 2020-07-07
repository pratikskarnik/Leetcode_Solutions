class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros=nums.count(0)
        ones=nums.count(1)
        i=0
        while(i<len(nums)):
            if i<zeros:
                nums[i]=0
            elif i<zeros+ones:
                nums[i]=1
            else:
                nums[i]=2
            i+=1
        