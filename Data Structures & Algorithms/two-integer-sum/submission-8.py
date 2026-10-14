class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # early exit, if length = 2, return [0, 1]
        # brute force: loop through every element, loop through every num for diff

        if len(nums) == 2:
            return [0, 1]

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]  