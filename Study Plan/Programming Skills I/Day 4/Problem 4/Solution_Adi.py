class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        # find the first index where s1 and s2 differ
        index_diff = -1
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                index_diff = i
                break

        # if there is no difference, or more than one difference, we can't make them equal with a single swap
        if index_diff == -1 or sum(1 for i in range(len(s1)) if s1[i] != s2[i]) > 2:
            return False

        # check if swapping the characters at index_diff in s1 would make s1 equal to s2
        index_swap = -1
        for i in range(index_diff+1, len(s1)):
            if s1[i] == s2[index_diff] and s2[i] == s1[index_diff]:
                index_swap = i
                break

        return index_swap != -1
