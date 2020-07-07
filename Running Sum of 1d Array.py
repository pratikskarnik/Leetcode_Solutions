class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum1=0
        runsum=[]
        for i in nums:
            sum1+=i
            runsum.append(sum1)
        return runsum