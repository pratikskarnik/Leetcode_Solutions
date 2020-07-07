class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arr1=[-1]
        i=len(arr)-1
        max1=arr[i]
        while(i>=0):
            if max1<=arr[i]:
                max1=arr[i]
            arr1.append(max1)
            i-=1
        arr1.pop()
        arr1.reverse()
            
        return arr1
            
        