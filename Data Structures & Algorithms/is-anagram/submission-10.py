class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # can use Collections.Counter for a lot shorter

        return Counter(s) == Counter(t)