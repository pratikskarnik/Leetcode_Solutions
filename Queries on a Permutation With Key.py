class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        list1=[x for x in range(1,m+1)]
        list2=[]
        for i in queries:
            index1=list1.index(i)
            list2.append(index1)
            for j in range(index1,0,-1):
                list1[j]=list1[j-1]
            list1[0]=i
        return list2
                
                