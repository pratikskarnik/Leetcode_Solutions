class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words=sentence.split(" ")
        for i in range(len(words)):
            a=words[i]
            if searchWord==a[0:len(searchWord)]:
                return i+1
        return -1
        