class Solution:
    def reverse(self, x: int) -> int:
        ret = 0
        negative = True if x < 0 else False
        limit = 2**31 if negative else 2**31 - 1
        x = abs(x)
        dupe_x = x
        magnitude = 0
        while dupe_x:
            dupe_x //= 10
            magnitude += 1
        potentially_over = True if magnitude >= 10 else False
        while x:
            digit = x % 10
            if potentially_over:
                if negative:
                    if ret * 10 == (limit // 10 ** (magnitude - 1)) - (limit // 10 ** (magnitude - 1)) % 10 and digit > (limit // 10 ** (magnitude - 1)) % 10:
                        return 0
                else:
                    if ret * 10 == (limit // 10 ** (magnitude - 1)) - (limit // 10 ** (magnitude - 1)) % 10 and digit > (limit // 10 ** (magnitude - 1)) % 10:
                        return 0
            ret = ret * 10 + digit
            x //= 10
            magnitude -= 1
        return -ret if negative else ret
