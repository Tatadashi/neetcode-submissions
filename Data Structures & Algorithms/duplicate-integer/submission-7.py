class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # brute force is to loop through nums, populate arr
        # loop through arr, check for count > 1

        # declare hashset
        # loop through nums, adding nums to hashset
        # if already in hashset, return True
        # return False
        hset = set()

        for num in nums:
            if num in hset:
                return True
            hset.add(num)
        
        return False