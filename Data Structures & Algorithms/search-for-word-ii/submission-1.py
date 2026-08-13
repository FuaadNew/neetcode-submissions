class TrieNode:
    def __init__(self):
        self.children = {}
        self.val = ""
        self.isWord = False
class Trie:
    def __init__(self):
        self.Trie = TrieNode()

    def addWord(self, word):
        curr = self.Trie
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
                curr.children[c].val = c
            curr = curr.children[c]
        curr.isWord = True

    def print_words(self):
        def dfs(curr, path):
            if curr.isWord:
                print("".join(path))
                curr.isWord = False
                return
            for child in curr.children:
                path.append(curr.children[child].val)
                dfs(curr.children[child],path.copy())
        curr = self.Trie
        
        for child in curr.children:
            dfs(curr.children[child], [curr.children[child].val])



class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS,COLS = len(board),len(board[0])
        root = Trie()
        for word in words:
            root.addWord(word)
        res = []

        def dfs(r,c, curr,visit,  path, parent):
            if (r,c) in visit:
                return
            if curr.isWord:
                curr.isWord = False
                res.append("".join(path))
            visit.add((r,c))
            if (c - 1) >=0:
                char = board[r][c-1]
                if char in curr.children:
                    path.append(char)
                    dfs(r,c-1, curr.children[char], visit, path, curr)
                    path.pop()
            if (c + 1) < COLS:
                char = board[r][c+1]
                if char in curr.children:
                    path.append(char)
                    dfs(r,c+1, curr.children[char],visit, path,curr)
                    path.pop()
            if (r - 1) >= 0:
                char = board[r - 1][c]
                if char in curr.children:
                    path.append(char)
                    dfs(r-1,c, curr.children[char],visit, path,curr)
                    path.pop()
            if (r + 1) < ROWS:
                char = board[r + 1][c]
                if char in curr.children:
                    path.append(char)
                    dfs(r+1,c, curr.children[char],visit, path,curr)
                    path.pop()
            visit.remove((r,c))
            if not curr.isWord and not curr.children:
                del parent.children[curr.val]
            

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] not in root.Trie.children:
                    continue
                else:
                    char = board[r][c]
                    dfs(r,c,root.Trie.children[char], set(),[char], root.Trie)
    
        return res
                    
        #brute force search
        #only on characters that are starts of words?
        #only go in directions that are children. to the current node? 