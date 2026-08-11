class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr =  self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True


        

    def search(self, word: str) -> bool:
        curr = self.root
        def dfs(curr, i):
            if i == len(word):
                return curr.isWord
            if word[i] != "." and word[i] not in curr.children:
                return False
            if word[i] == ".":
                for child in curr.children:
                    if dfs(curr.children[child],i + 1):
                        return True
                return False
            else:
                return dfs(curr.children[word[i]], i + 1)

        return dfs(curr,0)
