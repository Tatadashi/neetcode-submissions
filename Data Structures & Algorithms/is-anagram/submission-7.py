class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if 2 str different len, return False
        # 2 hmap (key: letter, value: count)
        # loop thru s, hmap 1
        # loop thru t, hmap 2
        # compare hmap1 and hmap 2
        #   return True if same
        # return False

        if len(s) != len(t):
            return False
        
        hmapS = defaultdict(int)
        hmapT = defaultdict(int)

        for i in s:
            hmapS[i] += 1

        for i in t:
            hmapT[i] += 1

        if hmapS == hmapT:
            return True

        return False    