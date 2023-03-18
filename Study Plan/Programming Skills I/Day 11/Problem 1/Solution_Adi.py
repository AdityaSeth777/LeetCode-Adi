from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # define a custom comparison function
        def bit_count(num):
            # count the number of ones in the binary representation of the number
            count = 0
            while num:
                count += num & 1
                num >>= 1
            return count

        # sort the array using the custom comparison function
        arr.sort(key=lambda x: (bit_count(x), x))

        return arr
