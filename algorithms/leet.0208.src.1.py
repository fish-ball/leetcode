class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.value = ''
        self.children = [None] * 26
        self.end = False


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        k = ord(word[0]) - 97
        nxt = self.children[k] = self.children[k] or Trie()
        nxt.value = word[0]
        if len(word) == 1:
            nxt.end = True
        else:
            nxt.insert(word[1:])


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if not word:
            return self.end
        k = ord(word[0]) - 97
        if not self.children[k]:
            return False
        return self.children[k].search(word[1:])


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        if not prefix:
            return True
        k = ord(prefix[0]) - 97
        if not self.children[k]:
            return False
        return self.children[k].startsWith(prefix[1:])



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
