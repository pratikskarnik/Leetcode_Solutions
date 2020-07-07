class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        set1=set(nums)
        set2=[x for x in range(1,n+1)]
        set2=set(set2)
        set3=set2-set1
        set3=list(set3)
        return set3