from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Create an empty set to store the unique elements of nums
        unique_nums = set()

        # Iterate over each element in nums
        for num in nums:
            # If the element is already in the set, it means it has occurred before
            # so we return True
            if num in unique_nums:
                return True

            # Otherwise, add the element to the set
            unique_nums.add(num)

        # If we have iterated over all elements and none of them have occurred before,
        # we return False
        return False
