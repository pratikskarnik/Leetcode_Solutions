class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        median=arr[(len(arr)-1)//2]
        c=[]
        for i in range(len(arr)):
            j=abs(arr[i]-median)
            c.append([arr[i],j])
        c.sort(key=lambda c:(c[1],c[0]), reverse=True)
        d=[]
        for i in range(k):
            d.append(c[i][0])
        return d