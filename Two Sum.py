class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dummy=[]
        for i in nums:
            dummy.append(target-i)
        nums2=set(nums)
        dummy=set(dummy)
        element3=nums2.intersection(dummy)
        element3=list(element3)
        if len(element3)>2:
            for i in element3:
                if target==2*i:
                    element3.remove(i)
        print(element3)
        if len(element3)==1:
            indices=[]
            for i in range(len(nums)):
                if nums[i]==element3[0]:
                    indices.append(i)
            return indices
                    
        elepos=nums.index(element3[0])
        elepos2=nums.index(element3[1])
        return [elepos,elepos2]
            
        