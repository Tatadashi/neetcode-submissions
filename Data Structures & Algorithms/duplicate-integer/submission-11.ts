class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums: number[]): boolean {
        // convert nums to set
        // compare length of nums and set
        // if set smaller than nums, are dupes, return True
        let seen: Set<number> = new Set(nums);
        return seen.size < nums.length;
    }
}
