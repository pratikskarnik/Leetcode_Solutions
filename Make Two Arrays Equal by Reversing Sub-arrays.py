class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        flag=True
        for i in arr:
            if i not in target:
                flag=False
        return flag
        