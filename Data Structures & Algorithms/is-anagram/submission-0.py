class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        
        chars_s = {}
        chars_t = {}

        for char in s:
            if char in chars_s:
                chars_s[char] += 1
            else:
                chars_s[char] = 1
        
        for char in t:
            if char in chars_t:
                chars_t[char] += 1
            else:
                chars_t[char] = 1
        
        return chars_s == chars_t
        