class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(path, visited):
            if len(path) == len(nums):
                res.append(path)
                return
            
            for i in range(len(nums)):
                if nums[i] not in visited:
                    visited.add(nums[i])
                    dfs(path + [nums[i]], visited)
                    visited.remove(nums[i])
        
        dfs([], set())
        return res