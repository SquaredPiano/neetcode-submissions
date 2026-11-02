class Solution:
    def trap(self, height: List[int]) -> int:        
        l = 0
        r = len(height) - 1
        currMin = 0
        total = 0
        while l <= r:
            left_height = max(height[l], currMin)
            total += left_height - height[l]
            
            if l == r:
                break
            
            right_height = max(height[r], currMin)
            total += right_height - height[r]

            currMin = min(left_height, right_height)

            if left_height < right_height:
                l += 1
            elif left_height > right_height:
                r -= 1
            else:
                l += 1
                r -= 1
        return total