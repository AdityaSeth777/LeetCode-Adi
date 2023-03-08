class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # If both low and high are odd, then there will be (high-low)/2+1 odd numbers
        if low % 2 == 1 and high % 2 == 1:
            return (high - low) // 2 + 1
        
        # If both low and high are even, then there will be (high-low)/2 odd numbers
        if low % 2 == 0 and high % 2 == 0:
            return (high - low) // 2
        
        # If low is even and high is odd, then there will be (high-low+1)/2 odd numbers
        # If low is odd and high is even, then there will be (high-low-1)/2+1 odd numbers
        return (high - low + 1) // 2
