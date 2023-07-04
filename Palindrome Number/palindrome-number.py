class Solution:
    def isPalindrome(self, x: int) -> bool:
        a=list(str(x))
        b=list(str(x))
        b.reverse()
        return True if a==b else False