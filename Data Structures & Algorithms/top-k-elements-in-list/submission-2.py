class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return list(set(nums))  

        frequencies = defaultdict(int)
        for num in nums:
            frequencies[num] += 1
        
        return sorted(frequencies, key=frequencies.get, reverse=True)[:k]