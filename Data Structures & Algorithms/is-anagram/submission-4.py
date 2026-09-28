class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # want a make a dict, populate it,
        count: dict[str, int] = {}

        if (len(s) != len(t)):
            return False

        for i in range(len(s)):
            if (s[i] in count):
                count[s[i]] += 1
            else:
                count[s[i]] = 1
        
        for i in range(len(t)):
            if (t[i] not in count):
                return False
    
            count[t[i]] -= 1
            if (count[t[i]] < 0):
                return False

        return True