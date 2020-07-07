class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A)<3:
            return False
        flag=False
        for h in range(len(A)-1):
            if A[h]<A[h+1]:
                flag= True
                break
        if flag:
            flag=False
            for i in range(len(A)-1):
                if A[i]>A[i+1]:
                    break
                if A[i]==A[i+1]:
                    return False
            for j in range(i,len(A)-1):
                if A[j]>A[j+1]:
                    flag=True
                    break
            for k in range(j,len(A)-1):
                if A[k]<=A[k+1]:
                    flag=False
                    break
        return flag