class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums2=set(nums)
        nums3=[]
        for i in nums2:
            nums3.append((i,nums.count(i)))
        for i in nums3:
            for j in range(i[1]-1):
                nums.remove(i[0])
        return len(nums)
        