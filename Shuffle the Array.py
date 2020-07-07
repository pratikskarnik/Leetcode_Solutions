class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        a=nums[:len(nums)//2]
        b=nums[len(nums)//2:]
        print(a)
        print(b)
        c=[]
        for i in range(len(nums)//2):
            c.append(a[i])
            c.append(b[i])
        return c