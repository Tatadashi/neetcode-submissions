class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a hashmap of letters for each str (group by anagram)
            # key: ['a': 0, ...] value: ["word", ...]
        # for loop through every str in list
            # create a letter hashtable for current str
                # arr where index is ASCII letter - ASCII 'a'
                # value is count
            # put word into hashmap if exists, or create new entry
        # return all values in hashmap
        
        anagrams = {}

        for word in strs:
            counts = [0] * 26
            for letter in word:
                counts[ord(letter) - ord('a')] += 1
            currList = anagrams.get(tuple(counts), [])
            currList.append(word)
            anagrams[tuple(counts)] = currList
        
        return list(anagrams.values())