Problem -> <https://leetcode.com/problems/contains-duplicate/description/?envType=study-plan&id=programming-skills-i>


In this implementation, we first create an empty set unique_nums to store the unique elements of nums.

We then iterate over each element in nums. If the element is already in the set unique_nums, it means it has occurred before, so we return True, indicating that there is at least one duplicate element in nums.

Otherwise, we add the element to the set unique_nums. If we have iterated over all elements and none of them have occurred before, we return False, indicating that every element is distinct.
