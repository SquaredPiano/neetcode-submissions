class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for s in strs:
            ret += s + "é"
        return ret
    def decode(self, s: str) -> List[str]:
        temp = s.split("é")
        temp.pop()
        return temp