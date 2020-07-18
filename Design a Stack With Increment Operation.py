class CustomStack:

    def __init__(self, maxSize: int):
        self.arr=[]
        self.maxSize=maxSize
        

    def push(self, x: int) -> None:
        if len(self.arr)<self.maxSize:
            self.arr.insert(0,x)
        

    def pop(self) -> int:
        if len(self.arr)==0:
            return -1
        return self.arr.pop(0)
        

    def increment(self, k: int, val: int) -> None:
        i=len(self.arr)-1
        while(k>0 and i>=0):
            self.arr[i]+=val
            i-=1
            k-=1
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)