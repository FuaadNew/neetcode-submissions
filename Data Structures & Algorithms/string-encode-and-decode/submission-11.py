class Solution:

    def encode(self, strs: List[str]) -> str:
        res = "".join( f"{len(word)}" + "#" + word for word in strs)
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
                word = s[j + 1: j + length + 1]
                res.append(word)
            i = j + length + 1
           
        return res

                
        
