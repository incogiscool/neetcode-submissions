class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = {} # Gonna make the key a tuple of the arr of chars, val is arr of anagrams

        for word in strs:
            count = [0] * 26 # 26 letters in lowercase english alphabet

            for char in word:
                idx = ord(char) - ord("a") # Gonna use "a" as the datum for ascii chars

                count[idx] += 1
            
            key = tuple(count)

            if key in res:
                res[key].append(word)
            else:
                res[key] = [word]

        return list(res.values())

