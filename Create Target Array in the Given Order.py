class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        nums2=[]
        for i in range(len(nums)):
            nums2.insert(index[i],nums[i])
        return nums2
        