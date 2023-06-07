from collections import Counter

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = Counter({0: 1})
        mod = 10 ** 9 + 7
        for i in range(1, high + 1):
            
            z = dp[i - zero]
            
            o = dp[i - one]
            
            n = (z + o) % mod
           
            dp[i] = n
        
        
        ans = sum(dp[i] for i in range(low, high + 1)) % mod
        
     
        return ans