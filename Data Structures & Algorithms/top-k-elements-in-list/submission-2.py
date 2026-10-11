class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = defaultdict(int)
        for num in nums:
            freq_dict[num] += 1

        max_freq = max(freq_dict.values())
        buckets = [[] for _ in range(max_freq)]
        for num, freq in freq_dict.items():
            buckets[freq - 1].append(num)
        
        res = []
        for i in range(len(buckets) - 1, -1, -1):
            res.extend(buckets[i])
            if len(res) == k:
                return res