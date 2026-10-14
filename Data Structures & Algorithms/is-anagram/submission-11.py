class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # trying enumerate
        if len(s) != len(t):
            return False

        counts = [0] * 26
        for i, num in enumerate(s):
            counts[ord(num) - ord('a')] += 1
        
        for i, num in enumerate(t):
            counts[ord(num) - ord('a')] -= 1

        for val in counts:
            if val != 0:
                return False
        
        return True