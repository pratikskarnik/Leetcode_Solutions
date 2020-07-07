class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums2=[]
        for i in nums:
            count=0
            for j in nums:
                if j<i:
                    count+=1
            nums2.append(count)
        return nums2
                    
        