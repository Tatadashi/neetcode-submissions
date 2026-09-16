class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums: number[], target: number): number[] {        
        if (nums.length == 2) {
            return [0, 1];
        }

        for (let i: number = 0; i < nums.length; i++) {
            for (let j: number = nums.length; j > i; j--) {
                if (nums[i] + nums[j] == target) {
                    return [i, j];
                }
            }
        }
    }
}
