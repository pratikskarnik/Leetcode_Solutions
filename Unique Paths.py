class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        path=[1 for i in range(n)]
        for i in range(m-1):
            for j in range(1,n):
                path[j]+=path[j-1]
        return path[n-1]
        