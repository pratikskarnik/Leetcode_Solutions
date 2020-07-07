class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        for i in nums:
            j=int(log10(i))
            if j%2==1:
                count+=1
        return count
                