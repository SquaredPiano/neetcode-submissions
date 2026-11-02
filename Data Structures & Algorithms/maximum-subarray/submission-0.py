class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = -float('inf')
        max_sum = -float('inf')
        for num in nums:
            curr_sum = max(curr_sum + num, num)
            max_sum = max(curr_sum, max_sum)
        return max_sum