class Solution:

    def encode(self, strs: List[str]) -> str:
        res = "".join([str(len(word)) + "#" + word for word in strs ])
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                j = i
                while s[j].isdigit():
                    j+=1
                length = int(s[i:j])
                res.append(s[j + 1: j + 1  + length])
                i+= (j - i) + 1 + length
    
        return res

        
