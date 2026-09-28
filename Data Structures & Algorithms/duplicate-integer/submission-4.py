class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return False

        unique: Set[int] = set()
        for num in nums:
            if num in unique:
                return True
            unique.add(num)
        
        return False