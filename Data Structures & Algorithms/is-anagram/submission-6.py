class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # want a make a dict, populate it,
        s_letters: dict[str, int] = {}
        t_letters: dict[str, int] = {}

        if (len(s) != len(t)):
            return False

        for char in s:
            if (char in s_letters):
                s_letters[char] += 1
            else:
                s_letters[char] = 1
        
        for char in t:
            if (char in t_letters):
                t_letters[char] += 1
            else:
                t_letters[char] = 1

        if (s_letters == t_letters):
            return True
        
        return False
            