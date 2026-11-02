from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        cntr_s = Counter(s)
        cntr_t = Counter(t)

        for char in cntr_t:
            if not char in cntr_s or cntr_s[char] < cntr_t[char]:
                return ""
        
        l = 0
        curr_window = Counter()
        satisfied = {}
        res = s
        count_satisfied = 0
        for r in range(len(s)):
            if s[r] in cntr_t:
                curr_window[s[r]] = curr_window.get(s[r], 0) + 1
                if curr_window[s[r]] >= cntr_t[s[r]]:
                    if s[r] not in satisfied or not satisfied[s[r]]:
                        count_satisfied += 1
                    satisfied[s[r]] = True
                    
            
            while count_satisfied == len(cntr_t):
                if s[l] in curr_window:
                    curr_window[s[l]] -= 1
                    if curr_window[s[l]] < cntr_t[s[l]]:
                        if r - l + 1 < len(res):
                            res = s[l:r+1]
                        satisfied[s[l]] = False
                        count_satisfied -= 1

                l += 1
            
        return res
            
