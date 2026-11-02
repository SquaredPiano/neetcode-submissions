class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left = 0
        right = len(heights) - 1

        maxWater = 0
        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            maxWater = max(maxWater, width*height)
            if heights[left] < heights[right]:
                left += 1
            elif heights[right] < heights[left]:
                right -= 1
            else:
                left += 1
                right -= 1
        
        return maxWater