class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(start, path):
            print(start, path)
            if start >= len(nums):
                res.append(path)
                return
            
            dfs(start + 1, path + [nums[start]])
            i = start
            while i + 1 <= len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1, path)
        
        dfs(0, [])
        return res