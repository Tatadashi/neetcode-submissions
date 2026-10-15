class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums: number[], target: number): number[] {
        // hashmap (key: num, value: index)
            // represents prev values checked in for loop
        // iterate over nums
            // check if diffValue (target - currentValue) is in prev
                // return [prev[diffValue], currentIndex]
            // add currentValue:currentIndex into prev

        const prev: Map<number, number> = new Map();

        for (let i: number = 0; i < nums.length; i++) {
            let diff: number = target - nums[i];
            if (prev.has(diff)) {
                return [prev.get(diff), i];
            }
            
            prev.set(nums[i], i);
        }
    }
}
