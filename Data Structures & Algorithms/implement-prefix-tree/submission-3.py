class TrieNode:
    def __init__(self):
        self.val = ""
        self.children = {}
        self.endWord = False


class PrefixTree:

    def __init__(self):
        self.Trie = TrieNode()

        

    def insert(self, word: str) -> None:
        curr = self.Trie
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
                curr.children[c].val = c
            curr = curr.children[c]
        curr.endWord = True
       
        

    def search(self, word: str) -> bool:
        curr = self.Trie
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.endWord
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.Trie
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)