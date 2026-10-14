class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # best way
        # convert nums to hashset
        # compare length of nums to hashset
        # if equal, no duplicates, return False
        # return True

        seen = set(nums)
        return len(seen) < len(nums)