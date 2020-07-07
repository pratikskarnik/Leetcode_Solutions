class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        sets=[]
        for i in favoriteCompanies:
            sets.append(set(i))
        set1=[]
        for i in range(len(sets)):
            flag=False
            for j in range(len(sets)):
                if sets[i]!=sets[j] and sets[i].issubset(sets[j]):
                    flag=True
                    break
            if not flag:
                set1.append(i)
        return set1
                    