class Solution:
    def reverse(self, x: int) -> int:
        is_neg = x < 0
        x =abs(x)
        res = 0
        while x > 0:
            digit = x % 10
            x = x //10
            res = res * 10 + digit
            if res > 2**31-1:
                return 0
        return res if not is_neg else -res
        