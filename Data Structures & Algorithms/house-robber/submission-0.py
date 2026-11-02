class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]

        dp = [0] * (len(nums))
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])
        max_sum = 0
        for i in range(2, len(nums)):
            incl = nums[i] + dp[i - 2]
            excl = dp[i - 1]
            dp[i] = max(incl, excl)
        
        return dp[-1]