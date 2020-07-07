class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        mat=[[0 for x in range(m)] for y in range(n)]
        for i in indices:
            row = i[0]
            col = i[1]
            for i in range(m):
                mat[row][i]+=1
            for i in range(n):
                mat[i][col]+=1
        count=0
        print(mat)
        for x in range(n):
            for y in range(m):
                if (mat[x][y])&1==1:
                    count+=1
        return count
        