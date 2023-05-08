class Solution:
    # dictionary to store previously computed substrings
    map = {}

    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)
        # check if the two strings are equal
        if s1 == s2:
            return True
        # initialize frequency lists for s1, s2, and current substring
        a, b, c = [0] * 26, [0] * 26, [0] * 26
        # check if the current substring has already been computed
        if (s1 + s2) in self.map:
            return self.map[s1 + s2]
        # check all possible splits of the two strings
        for i in range(1, n):
            j = n - i
            # update frequency lists for s1, s2, and current substring
            a[ord(s1[i - 1]) - ord('a')] += 1
            b[ord(s2[i - 1]) - ord('a')] += 1
            c[ord(s2[j]) - ord('a')] += 1
            # check if the current substring has the same characters
            if a == b and self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                # if the substrings are scrambled versions of each other, return True
                self.map[s1 + s2] = True
                return True
            # check if the current substring and its complement have the same characters
            if a == c and self.isScramble(s1[:i], s2[j:]) and self.isScramble(s1[i:], s2[:j]):
                # if the substrings are scrambled versions of each other, return True
                self.map[s1 + s2] = True
                return True
        # if none of the splits result in scrambled versions, return False
        self.map[s1 + s2] = False
        return False