class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr=[]
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        self.arr.append(word)
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if word in self.arr:
            return True
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        prefixlen=len(prefix)
        for word in self.arr:
            if word[:prefixlen]==prefix:
                return True
        return False
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)