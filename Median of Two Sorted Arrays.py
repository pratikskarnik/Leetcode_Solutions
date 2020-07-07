class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i=0
        j=0
        nums3=[]
        while(i<len(nums1) and j<len(nums2)):
            if nums1[i]<=nums2[j]:
                nums3.append(nums1[i])
                i+=1
            else:
                nums3.append(nums2[j])
                j+=1
        if i==len(nums1):
            while(j<len(nums2)):
                nums3.append(nums2[j])
                j+=1
        elif j==len(nums2):
            while(i<len(nums1)):
                nums3.append(nums1[i])
                i+=1
        print(nums3)
        l=len(nums3)
        if l%2==1:
            return nums3[(l//2)]
        else:
            return (nums3[(l//2)-1]+nums3[(l//2)])/2
            
            
        