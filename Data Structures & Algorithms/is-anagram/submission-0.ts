class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s: string, t: string): boolean {
        if (s.length != t.length) {
            return false;
        }

        const sHM: Map<string, number> = new Map(); 
        const tHM: Map<string, number> = new Map(); 

        for (let i: number = 0; i < s.length; i++) {
            if (sHM.has(s[i])) {
                sHM.set(s[i], sHM.get(s[i]) + 1)
            } else {
                sHM.set(s[i], 1);
            }

            if (tHM.has(t[i])) {
                tHM.set(t[i], tHM.get(t[i]) + 1)
            } else {
                tHM.set(t[i], 1);
            }
            
        }

        for (const [letter, count] of sHM) {
            if (!tHM.has(letter)) {
                return false;
            }

            if (count != tHM.get(letter)) {
                return false;
            }
        }

        return true;
    }
}
