class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        elif len(s) == 1:
            return 1
        
        dupes = set()
        l = 0
        maxCount = 0
        for r in range(len(s)):
            while s[r] in dupes:
                dupes.remove(s[l])
                l += 1
            dupes.add(s[r])
            maxCount = max(maxCount, r - l + 1)

        return maxCount
