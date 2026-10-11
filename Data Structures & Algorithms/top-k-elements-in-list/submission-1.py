class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = defaultdict(int)
        rev_freq_dict = defaultdict(list)
        for num in nums:
            freq_dict[num] += 1

        for num in freq_dict:
            freq = freq_dict[num]
            rev_freq_dict[freq].append(num)

        max_freq = max(rev_freq_dict.keys())
        buckets = [[] for _ in range(max_freq)]
        for freq in rev_freq_dict:
            buckets[freq - 1].extend(rev_freq_dict[freq])
        
        res = []
        for i in range(len(buckets) - 1, -1, -1):
            res.extend(buckets[i])
            if len(res) == k:
                return res