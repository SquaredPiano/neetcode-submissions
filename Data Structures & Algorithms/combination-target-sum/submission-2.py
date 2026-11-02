class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(start, path, curr):
            if curr > target or start >= len(nums):
                return
            elif curr == target:
                res.append(path.copy())
                return
            
            path.append(nums[start])
            dfs(start, path, curr + nums[start])
            path.pop()
            dfs(start + 1, path, curr)

        
        dfs(0, [], 0)

        return res