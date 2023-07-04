class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # initialize dictionaries to keep track of character frequency
        s_freq = {}
        t_freq = {}

        # count frequency of characters in s
        for char in s:
            s_freq[char] = s_freq.get(char, 0) + 1

        # count frequency of characters in t
        for char in t:
            t_freq[char] = t_freq.get(char, 0) + 1

        # compare the frequencies to find the extra character
        for char in t_freq:
            if char not in s_freq or t_freq[char] != s_freq[char]:
                return char