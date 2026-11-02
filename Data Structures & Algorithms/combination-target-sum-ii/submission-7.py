class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        print(candidates)
        def dfs(start, path, total):
            if total == target:
                res.append(path)
                return
            elif start >= len(candidates) or total > target:
                return

            dfs(start + 1, path + [candidates[start]], total + candidates[start])
            i = start
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, path, total)
            
        dfs(0, [], 0)
        return res