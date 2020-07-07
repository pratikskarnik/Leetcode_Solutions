class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i=0
        l=len(arr)
        arr2=[]
        for i in range(len(arr)):
            if arr[i]==0:
                arr2.append(i)
        j=1
        print(arr2)
        for i in arr2:
            arr.insert(i+j,0)
            arr.pop()
            j+=1
        