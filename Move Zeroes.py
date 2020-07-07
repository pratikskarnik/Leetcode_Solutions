class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count1=nums.count(0)
        for i in range(count1):
            nums.remove(0)
        for i in range(count1):
            nums.append(0)