class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        nei  = {}

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j+1:]
                if pattern not in nei:
                    nei[pattern] = set()
                nei[pattern].add(word)
        time = 1
        visit = {beginWord}
        q= deque([beginWord])

        while q:
            for i in range(len(q)):
                curr = q.popleft()
                for j in range(len(curr)):
                    pattern = curr[:j] + '*' + curr[j+1:]
                    if pattern in nei:
                        for neiword in nei[pattern]:
                            if neiword == endWord:
                                return time + 1
                            if neiword not in visit:
                                visit.add(neiword)
                                q.append(neiword)
            time+=1
        return 0
        
