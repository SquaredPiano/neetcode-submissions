class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapper = {}
        curr_ind = 0
        res = []
        for word in strs:
            c = [0] * 26
            for char in word:
                c[ord(char) - ord('a')] += 1
            c = tuple(c)
            if c not in mapper:
                mapper[c] = curr_ind
                curr_ind += 1
                res.append([word])
            else:
                res[mapper[c]].append(word)
        return res