class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        arr1= [ x for x in A if x&1==0]
        arr2= [ x for x in A if x&1==1]
        for i in arr2:
            arr1.append(i)
        return arr1