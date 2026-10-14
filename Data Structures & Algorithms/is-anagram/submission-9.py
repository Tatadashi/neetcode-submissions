class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return False if len(s) and len(t) not equal (early exit)
        # create hash table (arr) representing counts for all letters
        # loop through len(s), increment letters of s, decrement letters of t
        # loop through counts, return False if any letter is not 0
        # return True

        if len(s) != len(t):
            return False

        counts = [0] * 26
        for i in range(len(s)):
            counts[ord(s[i]) - ord('a')] += 1
            counts[ord(t[i]) - ord('a')] -= 1
        
        for val in counts:
            if val != 0:
                return False
        
        return True