class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        heights2=sorted(heights)
        count=0
        for i in range(len(heights)):
            if heights[i]!=heights2[i]:
                count+=1
        return count