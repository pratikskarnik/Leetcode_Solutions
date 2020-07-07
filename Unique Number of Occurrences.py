class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr2=set(arr)
        arr3=[arr.count(x) for x in arr2]
        arr4=set(arr3)
        if len(arr4)==len(arr3):
            return True
        else:
            return False
        