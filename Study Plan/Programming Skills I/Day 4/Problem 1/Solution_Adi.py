from typing import List

class Solution:
    def signFunc(self, x: int) -> int:
        if x == 0:
            return 0
        elif x > 0:
            return 1
        else:
            return -1

    def arraySign(self, nums: List[int]) -> int:
        product = 1
        for num in nums:
            product *= num
        return self.signFunc(product)
