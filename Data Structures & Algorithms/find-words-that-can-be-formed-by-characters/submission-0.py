class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0


        for word in words:
            wordCount = Counter(word)
            charsCount = Counter(chars)

            good = True
            for c in word:
                if c not in charsCount or charsCount[c] < wordCount[c]:
                    good = False
                    break
                wordCount[c]-=1
            if good:
                res+=len(word)
                

        return res

