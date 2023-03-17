class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        merged_str = ""

        while i < len(word1) and j < len(word2):
            merged_str += word1[i] + word2[j]
            i += 1
            j += 1

        if i < len(word1):
            merged_str += word1[i:]
        elif j < len(word2):
            merged_str += word2[j:]

        return merged_str
