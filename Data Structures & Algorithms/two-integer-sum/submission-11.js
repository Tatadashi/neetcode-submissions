class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        // create a hashmap (key: num, value: index)
            // represent prev values in the for loop
        // iterate over nums
            // get diffNum (target - currentNum)
            // check if diffNum in prevHMap
                // return [diffIndex, currentIndex]
            // add current to prevHMAP
        
        const prev = new Map();
        for (let i = 0; i < nums.length; i++) {
            let diff = target - nums[i];
            if (diff in prev) {
                return [prev[diff], i];
            }
            prev[nums[i]] = i; 
        }
    }
}
