class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        num=""
        for i in b:
            num+=str(i)
        num=int(num)
        return pow(a,num,1337)