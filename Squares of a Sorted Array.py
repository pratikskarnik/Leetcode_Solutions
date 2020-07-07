class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        B=[]
        for i in A:
            B.append(i*i)
        B.sort()
        return B
        