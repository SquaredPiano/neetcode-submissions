import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        heap = []
        for i in range(k - 1):
            heapq.heappush_max(heap, (nums[i], i))
        for l in range(len(nums) - k + 1):
            r = l + k - 1
            heapq.heappush_max(heap, (nums[r], r))
            curr_max, curr_max_ind = heap[0]
            while curr_max_ind < l:
                heapq.heappop_max(heap)
                curr_max, curr_max_ind = heap[0]
            res.append(curr_max)
        
        return res