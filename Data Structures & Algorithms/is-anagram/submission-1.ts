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
        for (let i: number = 0; i < s.length; i++) {
            if (sHM.has(s[i])) {
                sHM.set(s[i], sHM.get(s[i]) + 1)
            } else {
                sHM.set(s[i], 1);
            }
        }

        for (let i: number = 0; i < t.length; i++) {
            if (!sHM.has(t[i])) {
                return false;
            }

            sHM.set(t[i], sHM.get(t[i]) - 1);
            if (sHM.get(t[i]) < 0) {
                return false;
            }
        }

        return true;
    }
}
