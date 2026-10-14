class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # want a hash map that contains all previous (key: num, value: index)
            # of current in for loop
        # loop through nums
            # check if complement (target - current) is in prevMap
            # prev would have smaller index
            # add current to prevMap

        prev = {}
        for i, val in enumerate(nums):
            diff = target - val
            if diff in prev:
                return [prev[diff], i]
            prev[val] = i