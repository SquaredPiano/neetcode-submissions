class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        [1,2,-3,0,0]
        []
        """
        n = len(nums) # 5
        dupes = set() # set()
        for i, val in enumerate(nums):
            if val <= 0 or val >= n + 1 or val in dupes:
                nums[i] = 0 # [1, 2, -3, 0, 0], [1, 2, -3, 0, 0], [1, 2, 0, 0, 0]
            else:
                dupes.add(val) # {1, 2}
        
        # O(n)
        for i in range(n):
            val = nums[i]
            # can perform at most n swaps throughout the entire for loop
            # indepednndent of the for loop
            # so TOTAL times this while loop is ever touched is at most N
            # therefore, we can say this block is also O(n)
            
            # stop when lst[i] == 0 OR lst[i] == lst[val - 1]
            # loop condition should be the NOT of the above stop condition
            while not (nums[i] == 0 or nums[i] == nums[val - 1]): # [1, 2, 0, 0, 0]
            # perform swap such that lst[i] goes to lst[val - 1]
                nums[val - 1], nums[i] = nums[i], nums[val - 1]
                val = nums[i]
        
        # O(n)
        # returns 3 correctly
        for i, val in enumerate(nums):
            if val == 0:
                return i + 1
        return n + 1
