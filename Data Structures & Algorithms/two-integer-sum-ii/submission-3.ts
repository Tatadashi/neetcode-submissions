class Solution {
    /**
     * @param {number[]} numbers
     * @param {number} target
     * @return {number[]}
     */
    twoSum(numbers: number[], target: number): number[] {
        let left: number = 0;
        let right: number = numbers.length - 1
        const sums: number[] = [];

        while (left < right) {
            let currSum: number = (numbers[left] + numbers[right]);
            if (currSum == target) {
                sums.push(++left);
                sums.push(++right);
                return sums;
            }
            
            if (currSum > target) {
                right -= 1;
            } else if (currSum < target) {
                left += 1;
            }
        }

        return sums;
    }
}
