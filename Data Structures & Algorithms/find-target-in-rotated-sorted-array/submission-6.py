class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lIndex = 0
        rIndex = len(nums) - 1
        while (lIndex <= rIndex):
            mIndex = (lIndex + rIndex) // 2

            # check if any index = target
            if target == nums[lIndex]:
                return lIndex
            elif target == nums[rIndex]:
                return rIndex
            elif target == nums[mIndex]:
                return mIndex 

            #check if sorted 
            if nums[lIndex] > nums[mIndex]:
                if nums[mIndex] < target <= nums[rIndex]:
                    lIndex = mIndex + 1
                else:
                    rIndex = mIndex - 1

            else:
                if nums[lIndex] < target <= nums[mIndex]:
                    rIndex = mIndex - 1
                else:
                    lIndex = mIndex + 1
        
        return -1