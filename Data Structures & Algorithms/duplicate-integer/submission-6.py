class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # hashmap of values
        # check if hashmap value exists
        #   return true if so
        # return false

        hmap = defaultdict(int)
        for i in nums:
            if hmap[i] == 1:
                return True
            hmap[i] += 1
        
        return False