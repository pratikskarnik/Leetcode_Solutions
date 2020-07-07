class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        nums2=[]
        i=0
        while(i<len(nums)):
            for j in range(nums[i]):
                nums2.append(nums[i+1])
            i+=2
        return nums2
        