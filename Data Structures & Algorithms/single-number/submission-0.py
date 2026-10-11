class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        b = 0
        for num in nums:
            b ^= num
        return b