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
        count_satisfied = 0
        for r in range(len(s)):
            if s[r] in cntr_t:
                curr_window[s[r]] = curr_window.get(s[r], 0) + 1
                if curr_window[s[r]] >= cntr_t[s[r]]:
                    if s[r] not in satisfied or satisfied[s[r]] == False:
                        count_satisfied += 1
                    satisfied[s[r]] = True
                    
            
            while count_satisfied == len(cntr_t):
                if r - l + 1 < len(res):
                    res = s[l:r+1]

                if s[l] in curr_window:
                    curr_window[s[l]] -= 1
                    if curr_window[s[l]] < cntr_t[s[l]]:
                        satisfied[s[l]] = False
                        count_satisfied -= 1

                l += 1
            
        return res
            
