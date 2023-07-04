class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = ""
        # Every substring of length 1 is a palindrome
        for i in range(n):
            dp[i][i] = True
            ans = s[i]

        # Check for substrings of length 2
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                ans = s[i:i+2]

        # Check for substrings of length greater than 2
        for l in range(3, n+1):
            for i in range(n-l+1):
                j = i+l-1
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    ans = s[i:j+1]

        return ans