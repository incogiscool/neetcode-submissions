class Solution:

    def encode(self, strs: List[str]) -> str:
        string_concat = ""

        for string in strs:
            length = len(string)
            string_concat += f"{length}#{string}"

        print(string_concat)

        return string_concat

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0                          # start of the current chunk
        while i < len(s):
            j = s.index("#", i)        # find this chunk's delimiter
            length = int(s[i:j])       # digits between i and j
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length         # jump to the next chunk
        return res

