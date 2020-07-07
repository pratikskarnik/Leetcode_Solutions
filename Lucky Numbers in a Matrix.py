class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        minnum=[]
        for i in matrix:
            minnum.append(min(i))
        maxnum=[]
        for i in range(len(matrix[0])):
            max1=0
            for j in range(len(matrix)):
                if matrix[j][i]>max1:
                    max1=matrix[j][i]
            maxnum.append(max1)
        minnum=set(minnum)
        maxnum=set(maxnum)
        result=list(maxnum.intersection(minnum))
        return result
        