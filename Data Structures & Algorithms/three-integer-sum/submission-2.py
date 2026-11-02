class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                if num + nums[left] + nums[right] == 0:
                    res.append((num, nums[left], nums[right]))
                    left += 1
                    right -= 1
                    while left < len(nums) - 1 and nums[left] == nums[left - 1]:
                        left += 1
                    while right > i + 1 and nums[right] == nums[right + 1]:
                        right -= 1
                elif num + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1
        return res