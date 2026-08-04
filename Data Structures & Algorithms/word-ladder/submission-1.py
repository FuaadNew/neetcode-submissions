class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        time = 1
        wordList = set(wordList)
        q = deque([beginWord])
        visit = set()
        while q:
            for i in range(len(q)):
                curr = q.popleft()
                for i in range(len(curr)):
                    for letter in letters:
                        modify = list(curr)
                        if letter != modify[i]:
                            modify[i] = letter
                            check = "".join(modify)
                            if check in wordList and check not in visit:
                                visit.add(check)
                                if check == endWord:
                                    return time + 1
                                else:
                                    q.append(check)

            time+=1
        return 0