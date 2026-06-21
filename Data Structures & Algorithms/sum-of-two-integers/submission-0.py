class Solution:
    def getSum(self, a: int, b: int) -> int:
        bitshortener = 0xffffffff
        while (bitshortener & b) > 0:
            carry = (a & b) << 1
            a = (a ^ b)
            b = carry 
        return a & bitshortener if b > 0 else a