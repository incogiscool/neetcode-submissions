class Solution:

    def encode(self, strs: List[str]) -> str:
        string_concat = ""

        for string in strs:
            length = len(string)
            string_concat += f"{length}#{string}"

        print(string_concat)

        return string_concat

    def decode(self, s: str) -> List[str]:
        decoded_arr = []

        while s:
            i = s.index("#")
            count = int(s[:i])
            content = s[i + 1: i + count + 1]
            decoded_arr.append(content)
            clean = s[i + 1 + count:]
            s = clean
        
        return decoded_arr

