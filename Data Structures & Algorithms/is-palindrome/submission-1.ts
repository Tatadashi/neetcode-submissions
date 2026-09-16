class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s: string): boolean {
        if (s.length == 1) {
            return true;
        }

        let alphaNumericStr: string = s.replace(/[\W_]+/g, "").toLowerCase();

        for (let i: number = 0; i < alphaNumericStr.length; i++) {
            let left: string = alphaNumericStr[i];
            let right: string = alphaNumericStr[alphaNumericStr.length - 1 - i];
            if (left != right) {
                console.log(`left: ${left} right: ${left} ${right == left}`)
                return false;
            }
        } 

        return true;
    }
}
