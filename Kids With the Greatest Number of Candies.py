class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        a=[]
        max1=max(candies)
        for i in candies:
            if (i+extraCandies)>=max1:
                a.append(True)
            else:
                a.append(False)
        return a
        