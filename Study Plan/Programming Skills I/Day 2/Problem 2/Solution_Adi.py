class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        # Convert integer to string and split into a list of digits
        digits = [int(d) for d in str(n)]
        
        # Calculate the product and sum of the digits
        product = 1
        summation = 0
        for d in digits:
            product *= d
            summation += d
        
        # Return the difference between the product and sum of the digits
        return product - summation
