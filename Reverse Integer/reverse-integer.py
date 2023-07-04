class Solution:
    def reverse(self, x: int) -> int:
        # check if x is negative
        negative = x < 0
        
        # convert x to positive
        x = abs(x)
        
        # reverse the digits
        reversed_x = 0
        while x > 0:
            reversed_x = reversed_x * 10 + x % 10
            x //= 10
        
        # check for overflow condition
        if reversed_x > 2**31 - 1:
            return 0
        
        # convert back to negative if necessary
        if negative:
            reversed_x *= -1
        
        return reversed_x