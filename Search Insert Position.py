class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.binsearch(nums,0,len(nums)-1,target)
    
    
    def binsearch(self,nums: List[int],start:int,end:int,target:int)-> int:
        if start<=end:
            mid=start+(end-start)//2
            if nums[mid]==target:
                return mid
            elif target <nums[mid]:
                return self.binsearch(nums,start,mid-1,target)
            else:
                return self.binsearch(nums,mid+1,end,target)
        else:
            return start