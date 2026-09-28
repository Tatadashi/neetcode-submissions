class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return False

        seen: Dict[int, int] = {}
        for num in nums:
            if num not in seen:
                seen[num] = 1
            else:
                return True
        
        return False