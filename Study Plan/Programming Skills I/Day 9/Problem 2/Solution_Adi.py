class Solution:
    def freqAlphabets(self, s: str) -> str:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        result = ""
        i = 0
        while i < len(s):
            if i + 2 < len(s) and s[i+2] == "#":
                index = int(s[i:i+2])-1
                i += 3
            else:
                index = int(s[i])-1
                i += 1
            result += alphabet[index]
        return result
