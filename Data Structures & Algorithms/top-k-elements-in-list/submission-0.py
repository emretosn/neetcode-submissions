class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        s_counts = sorted(counts, key=counts.get, reverse=True)
        return s_counts[:k]