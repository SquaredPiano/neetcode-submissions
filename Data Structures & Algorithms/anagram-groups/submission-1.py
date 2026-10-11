class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapper = {}
        for word in strs:
            c = [0] * 26
            for char in word:
                c[ord(char) - ord('a')] += 1
            c = tuple(c)
            if c not in mapper:
                mapper[c] = [word]
            else:
                mapper[c].append(word)
        return list(mapper.values())