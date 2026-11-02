class Solution:
    def trap(self, height: List[int]) -> int:        
        l = 0
        r = len(height) - 1
        currMin = 0
        total = 0
        while l <= r:
            if height[l] < currMin:
                total += currMin - height[l]
                height[l] = currMin
            if height[r] < currMin:
                total += currMin - height[r]
                height[r] = currMin
            currMin = min(height[l], height[r])
            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else:
                l += 1
                r -= 1
        return total