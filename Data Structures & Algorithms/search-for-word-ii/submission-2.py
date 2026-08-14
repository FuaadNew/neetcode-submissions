class Trie:
    def __init__ (self):
        self.children = {}
        self.word = ""
        self.val = ""
    
    def addWord(self,word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = Trie()
            curr = curr.children[c]
            curr.val = c
        curr.word = word

    def printChildren(self):
        def dfs(curr):
            if curr.word:
                print(curr.word)
            for child in curr.children:
                dfs(curr.children[child])
        dfs(self)
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        def dfs(r,c,  curr, parent, visit):
            #print(curr.val)
            if curr.word:
                res.append(curr.word)
                curr.word = ""
            visit.add((r,c))
            #left c - 1
            if c - 1 >= 0 and board[r][c-1] in curr.children and (r,c - 1) not in visit:
                child_tile = board[r][c-1]
                dfs(r,c-1, curr.children[child_tile], curr, visit)
            #right c + 1
            if c + 1 < COLS and board[r][c+1] in curr.children and (r,c + 1) not in visit:
                child_tile = board[r][c+1]
                dfs(r,c+1, curr.children[child_tile], curr, visit)
            #up r + 1
            if r + 1 < ROWS and board[r + 1][c] in curr.children and (r + 1,c) not in visit:
                child_tile = board[r + 1][c]
                dfs(r + 1,c, curr.children[child_tile], curr, visit)
            #down r - 1
            if r - 1 >=0 and board[r - 1][c] in curr.children and (r - 1,c) not in visit:
                child_tile = board[r - 1][c]
                dfs(r - 1,c, curr.children[child_tile], curr, visit)
            
            visit.remove((r,c))
            if curr.word == "" and not curr.children:
                del parent.children[curr.val]
            
        ROWS,COLS = len(board),len(board[0])
        res = []
        root = Trie()
        for word in words:
            root.addWord(word)
        
        for r in range(ROWS):
            for c in range(COLS):
                char = board[r][c]
                if char not in root.children:
                    continue
                else:
                    dfs(r,c, root.children[char],root, set())
        return res

        