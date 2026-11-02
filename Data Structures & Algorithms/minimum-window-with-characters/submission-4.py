from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def isCounterSubset(d1: dict, d2: dict):
            """
            Returns True if d1 is a subset of d2
            else False.
            """
            for char in d1:
                if not (char in d2 and d2[char] >= d1[char]):
                    return False
            return True

        if len(s) < len(t):
            return ""
        
        cntr_t = Counter(t)
        cntr_s = Counter(s)

        if not isCounterSubset(cntr_t, cntr_s):
            return ""

        # we now know the substring at least exists in s
        l = 0
        curr_window = Counter()
        satisfied = {}
        res = s
        for r in range(len(s)):
            if s[r] in cntr_t:
                curr_window[s[r]] = curr_window.get(s[r], 0) + 1
                if curr_window[s[r]] >= cntr_t[s[r]]:
                    satisfied[s[r]] = True
            
            # while isCounterSubset(cntr_t, curr_window):
            while len(satisfied) == len(cntr_t) and all(satisfied.values()):
                if r - l + 1 < len(res):
                    res = s[l:r+1]

                left_char = s[l]
                if left_char in curr_window:
                    curr_window[s[l]] -= 1
                    if curr_window[s[l]] < cntr_t[s[l]]:
                        satisfied[s[l]] = False
                    
                l += 1
            
        return res
            
