from decimal import Decimal
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        if n<3:
            return n
        max2=0
        for i in points:
            d={}
            duplicates=0
            max1=0
            for j in points:
                if i!=j:
                    if i[0]==j[0]:
                        slope="inf"
                    else:
                        slope=Decimal(j[1]-i[1])/Decimal(j[0]-i[0])
                    d[slope]=d.get(slope,0)+1
                    max1=max(max1,d[slope])
                    
                else:
                    duplicates+=1
            max2=max(max1+duplicates,max2)
            
            
        return max2
            
        