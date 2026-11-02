class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        hashed_nums = set(nums)
        max_seq = 0
        for num in hashed_nums:
            if not num - 1 in hashed_nums:
                curr_seq = 1
                while num + curr_seq in hashed_nums:
                    curr_seq += 1
                max_seq = max(max_seq, curr_seq)
        return max_seq
        
            

        # lower_ranges = {}
        # upper_ranges = {}
        # for i, num in enumerate(nums):
        #     if not lower_ranges and not upper_ranges:
        #         lower_ranges[num] = i
        #         upper_ranges[num] = i
        #         continue
            
        #     if num - 1 in upper_ranges:
        #         stor = upper_ranges[num - 1]
        #         del upper_ranges[num - 1]
        #         if not num in upper_ranges:
        #             upper_ranges[num] = stor
        #         else:
        #             upper_ranges[]
        #     if num + 1 in lower_ranges:
        #         stor = lower_ranges[num + 1]
        #         del lower_ranges[num + 1]
        #         lower_ranges[num] = stor
            

        # # bucket = [None] * len(nums)
        # # dupes = set()
        # # lo = min(nums)
        # # hi = max(nums)
        # # for i, num in enumerate(nums):
        # #     nums[i] -= lo
        # #     if nums[i] >= len(nums) or nums[i] in dupes:
        # #         nums[i] = None
        # #     else:
        # #         dupes.add(nums[i])
        
        # # for i, num in enumerate(nums):
        # #     if num is not None:
        # #         bucket[nums[i]] = nums[i]

        # # maxSeq = 1
        # # currSeq = 0
        # # for i, num in enumerate(bucket):
        # #     if num is None:
        # #         maxSeq = max(maxSeq, currSeq)
        # #         currSeq = 0
        # #     else:
        # #         currSeq += 1
        # # return max(maxSeq, currSeq)