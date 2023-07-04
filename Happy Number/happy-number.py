class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_of_squares(num):
            sum_squares = 0
            while num > 0:
                digit = num % 10
                sum_squares += digit ** 2
                num //= 10
            return sum_squares
        
        seen = set()
        while n not in seen:
            seen.add(n)
            n = sum_of_squares(n)
            if n == 1:
                return True
        return False