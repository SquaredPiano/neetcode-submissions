class Solution:
    def reverse(self, x: int) -> int:
        ret = 0
        negative = True if x < 0 else False
        limit = 2**31 if negative else 2**31 - 1
        x = abs(x)
        while x:
            digit = x % 10
            if ret > (limit // 10) or ret == limit // 10 and digit > limit % 10:
                return 0
            ret = ret * 10 + digit
            x //= 10
        return -ret if negative else ret
