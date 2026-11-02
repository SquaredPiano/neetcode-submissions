class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = []
        for char in s:
            if ord('a') <= ord(char.lower()) <= ord('z') or char.isdigit():
                res.append(char.lower())
        
        cleaned = "".join(res)
        return cleaned == cleaned[::-1]