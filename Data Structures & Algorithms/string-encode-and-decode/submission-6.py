class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        sizes = []
        for s in strs:
            sizes.append(len(s))
        print(",".join(str(x) for x in sizes) + "#" + "".join(strs))
        return ",".join(str(x) for x in sizes) + "#" + "".join(strs)
    
    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sizes, strs = s.split("#", maxsplit=1)
        sizes = sizes.split(",")
        sizes = [int(size) for size in sizes]
        res = []
        str_ptr = 0
        for size in sizes:
            string = []
            for i in range(str_ptr, str_ptr + size):
                string.append(strs[i])
            str_ptr = str_ptr + size
            res.append("".join(string))
        return res
        # res = []
        # i = 0
        # while i < len(s):
        #     if s[i].isdigit() and i < len(s) - 1 and s[i + 1] == "#":
        #         i += 2
        #         end = i + int(s[i - 2])
        #         string = []
        #         while i < end:
        #             string.append(s[i])
        #             i += 1
        #         res.append("".join(string))
        # return res