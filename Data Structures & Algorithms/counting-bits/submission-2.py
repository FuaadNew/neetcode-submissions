class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        def count(i):
            string = str(bin(i))
            res = 0
            for char in string:
                if char == "1":
                    res+=1
            return res
        for i in range(0, n + 1):
            res.append(count(i))
        return res