class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(set(nums)) == k:
            return list(set(nums))
        
        seen = defaultdict(int)
        for num in nums:
            seen[num] += 1
        
        return sorted(seen, key=seen.get, reverse=True)[:k]