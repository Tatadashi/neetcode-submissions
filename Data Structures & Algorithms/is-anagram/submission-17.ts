class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s: string, t: string): boolean {
        // check if length of s and t equal, return if not (early exit)
        // make arr counts, acts as hashtable
            // index is ASCII of letter, value is count
        // loop through length of s or t, increment s letter, decrement t letter
        // use every to loop through counts, check if each letter 0
            // if so, return true, otherwise at the end return false

        if (s.length !== t.length) {
            return false;
        } 

        let counts: Array<number> = new Array(26).fill(0);
        for (let i: number = 0; i < s.length; i++) {
            counts[s.charCodeAt(i) - 'a'.charCodeAt(0)]++;            
            counts[t.charCodeAt(i) - 'a'.charCodeAt(0)]--;
        }

        return counts.every((val: number) => val === 0);
    }
}
