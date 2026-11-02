from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ana_occ = Counter(s1)

        l = 0
        sliding_window = Counter()
        sliding_window[s2[l]] = 1
        if sliding_window == ana_occ:
            return True

        for r in range(1, len(s2)):
            sliding_window[s2[r]] = sliding_window.get(s2[r], 0) + 1
            if r - l + 1 > len(s1):
                sliding_window[s2[l]] -= 1
                if sliding_window[s2[l]] == 0:
                    del sliding_window[s2[l]]
                l += 1
            
            if ana_occ == sliding_window:
                return True
        if ana_occ == sliding_window:
            return True
        return False