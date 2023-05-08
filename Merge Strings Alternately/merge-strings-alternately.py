import itertools
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return "".join(a+b for a, b in itertools.zip_longest(word1, word2, fillvalue=""))