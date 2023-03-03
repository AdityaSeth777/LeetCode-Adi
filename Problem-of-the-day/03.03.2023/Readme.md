Problem -> https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/submissions/908099816/

```The given code is an implementation of the strStr() function that takes two string arguments haystack and needle and returns the index of the first occurrence of needle in haystack or -1 if needle is not part of haystack. Let's break down the code and understand how it works:```

```bash
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
```

The code defines a class Solution and a method strStr() that takes two string arguments haystack and needle and returns an integer (the index of the first occurrence of needle in haystack).

```bash
    if not needle:
        return 0
    if not haystack:
        return -1
    if len(haystack) < len(needle):
        return -1
```

The first three lines are edge cases. If needle is an empty string, then it must be a substring of haystack starting from index 0, so we return 0. If haystack is an empty string or shorter than needle, then needle cannot be a substring of haystack, so we return -1.

```bash
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i+len(needle)] == needle:
            return i
```

Next, we loop through the haystack string using a sliding window of length len(needle). We start the loop from index 0 and end at the index len(haystack) - len(needle), since any substring of haystack that is shorter than needle cannot match needle.

Inside the loop, we check if the substring of haystack starting from index i and ending at index i + len(needle) matches needle. If it does, we return the starting index i of the substring in haystack.

```bash
    return -1
```

If we reach the end of the loop without finding a match, then needle is not a substring of haystack, so we return -1 to indicate that.