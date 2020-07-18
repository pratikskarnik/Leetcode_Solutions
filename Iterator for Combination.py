from itertools import combinations
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        list1=list(combinations(characters,combinationLength))
        self.arr=[]
        for i in list1:
            self.arr.append("".join(i))
        self.cursor=0
        

    def next(self) -> str:
        self.cursor+=1
        return self.arr[self.cursor-1]
        

    def hasNext(self) -> bool:
        if self.cursor<len(self.arr):
            return True
        return False
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()