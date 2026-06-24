class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charCount = Counter(chars)
        res = 0
        for word in words:
            good = True
            wordCount = Counter(word)
            for c in word:
                if wordCount[c] > charCount[c]:
                    good = False
                    print(c)
                    break
            if good:
                res+= len(word)
        return res
