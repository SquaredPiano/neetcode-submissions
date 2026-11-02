from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxCharCount = 1
        
        charOccurrences = defaultdict(int)
        charOccurrences[s[l]] += 1
        
        largestCharCount = 0
        for r in range(1, len(s)):
            charOccurrences[s[r]] += 1
            largestCharCount = max(charOccurrences[s[r]], largestCharCount)
            while r - l + 1 - largestCharCount > k:
                charOccurrences[s[l]] -= 1
                l += 1
            maxCharCount = max(maxCharCount, r - l + 1)
        return maxCharCount