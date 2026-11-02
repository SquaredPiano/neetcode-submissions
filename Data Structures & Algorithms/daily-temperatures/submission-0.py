class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, temperature in enumerate(temperatures):
            if not stack:
                stack.append((temperature, i))
                continue
            
            while stack and temperature > stack[-1][0]:
                res[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            
            stack.append((temperature, i))
        
        return res