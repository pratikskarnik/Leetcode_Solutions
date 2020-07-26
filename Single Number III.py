class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        list1=[]
        i=0
        while(i<len(nums)):
            n=nums[i]
            no1=nums.count(n)
            if no1==1:
                list1.append(n)
            i+=1
            
            
        return list1
        