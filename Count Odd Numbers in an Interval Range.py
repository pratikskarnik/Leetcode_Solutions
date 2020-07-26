class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low==high:
            if low&1==0:
                return 0
            else:
                return 1
        if low&1==0:
            low+=1
        if high&1==0:
            high-=1
        count=(high-low)/2
        count+=1
        return int(count)