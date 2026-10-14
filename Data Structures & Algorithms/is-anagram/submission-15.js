class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        // check if length of s and t are equal, return False if not (early exit)
        // create array representing hash table for letters and counts
        // loop through len(s) and increment letter of s and decrement letter of t

        if (s.length !== t.length) {
            return false;
        }

        const counts = new Array(26).fill(0);
        for (let i = 0; i < s.length; i++) {
            counts[s.charCodeAt(i) - 'a'.charCodeAt(0)]++;
            counts[t.charCodeAt(i) - 'a'.charCodeAt(0)]--;
        }

        return counts.every((val) => val === 0);
    }
}
