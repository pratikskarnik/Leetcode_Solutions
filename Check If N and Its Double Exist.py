class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr1=set(arr)
        arr2=[]
        for i in arr1:
            arr2.append(2*i)
        arr2=set(arr2)
        d=arr1.intersection(arr2)
        print(d)
        if 0 in d and arr.count(0)>1:
            return True
        if len(d)>0 and 0 not in d:
            return True
        if len(d)>1:
            return True
        
        return False