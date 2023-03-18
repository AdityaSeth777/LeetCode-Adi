class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If the length of s and t are not equal, they cannot be anagrams
        if len(s) != len(t):
            return False

        # Create a dictionary to count the frequency of characters in s
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1

        # Check if the frequency of characters in t matches that of s
        for char in t:
            if char not in freq or freq[char] == 0:
                return False
            freq[char] -= 1

        return True
