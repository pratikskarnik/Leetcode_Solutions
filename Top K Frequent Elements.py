class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        list1=[]
        nums2=set(nums)
        for i in nums2:
            list1.append((i,nums.count(i)))
        
        for i in range(k):
            for j in range(len(list1)-1):
                if list1[j][1]>list1[j+1][1]:
                    list1[j],list1[j+1]=list1[j+1],list1[j]
        list2=[]
        for i in range(k):
            list2.append(list1[len(list1)-i-1][0])
        return list2