class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        nei = defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                nei[pattern].append(word)

        num_of_words = 1
        visit = {beginWord}
        q = deque([beginWord])

        while q:
            for i in range(len(q)):
                curr = q.popleft()
                for j in range(len(curr)):
                    pattern = curr[:j] + "*" + curr[j+1:]
                    if pattern in nei:
                        for word in nei[pattern]:
                            if word == endWord:
                                return num_of_words + 1
                            if word not in visit:
                                visit.add(word)
                                q.append(word)
            num_of_words+=1

        
        return 0