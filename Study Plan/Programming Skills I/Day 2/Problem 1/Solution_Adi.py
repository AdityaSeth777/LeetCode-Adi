class Solution:
    def hammingWeight(self, n: int) -> int:
        # Initialize count to zero
        count = 0
        
        # Loop through all the bits in the binary representation of n
        while n > 0:
            # If the rightmost bit is 1, increment count
            if n & 1 == 1:
                count += 1
            # Shift n one bit to the right
            n = n >> 1
        
        # Return the count of '1' bits
        return count
