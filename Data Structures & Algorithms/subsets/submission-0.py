class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(start, path):
            if start >= len(nums):
                res.append(path)
                return
            
            dfs(start + 1, path + [nums[start]])
            dfs(start + 1, path)
        
        dfs(0, [])
        return res