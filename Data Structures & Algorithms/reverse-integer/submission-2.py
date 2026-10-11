class Solution:
    def reverse(self, x: int) -> int:
        ret = 0
        INT_MAX = 2**31 - 1
        INT_MIN = 2**31
        negative = True if x < 0 else False
        x = abs(x)
        dupe_x = x
        magnitude = 0
        while dupe_x:
            dupe_x //= 10
            magnitude += 1
        potentially_over = True if magnitude >= 10 else False
        while x:
            if potentially_over:
                if negative:
                    if ret * 10 == (INT_MIN // 10 ** (magnitude - 1)) - (INT_MIN // 10 ** (magnitude - 1)) % 10 and x % 10 > (INT_MIN // 10 ** (magnitude - 1)) % 10:
                        return 0
                else:
                    if ret * 10 == (INT_MAX // 10 ** (magnitude - 1)) - (INT_MAX // 10 ** (magnitude - 1)) % 10 and x % 10 > (INT_MAX // 10 ** (magnitude - 1)) % 10:
                        return 0
            ret *= 10
            ret += x % 10
            print("curr ret:", ret)
            x //= 10
            print("curr x", x)
            magnitude -= 1
        return -ret if negative else ret
