class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_to_letters = {'2': ["a", "b", "c"],
                          '3': ["d", "e", "f"],
                          '4': ["g", "h", "i"],
                          '5': ["j", "k", "l"],
                          '6': ["m", "n", "o"],
                          '7': ["p", "q", "r", "s"],
                          '8': ["t", "u", "v"],
                          '9': ["w", "x", "y", "z"]
        }
        res = []
        def dfs(i, path):
            if i == len(digits):
                if path:
                    res.append("".join(path[::]))
                return
            num = digits[i]
            for char in num_to_letters[num]:
                path.append(char)
                dfs(i+1, path)
                path.pop()
        dfs(0, [])
        return res