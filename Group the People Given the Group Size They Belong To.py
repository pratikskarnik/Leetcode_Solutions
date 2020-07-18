import numpy as np
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        list1=set(groupSizes)
        d={}
        for i in list1:
            list2=[]
            for j in range(len(groupSizes)):
                if i==groupSizes[j]:
                    list2.append(j)
            d.update({i:list2})
        list3=[]
        
        for i in list1:
            length=len(d[i])
            list4=d[i]
            if i!=length:
                div=length/i
                list4=np.array_split(list4,div)
                
                for i in list4:
                    list3.append(list(i))
            else:
                list3.append(list4)
        
        return list3
                