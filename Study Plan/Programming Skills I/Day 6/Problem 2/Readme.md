Problem -> <https://leetcode.com/problems/move-zeroes/description/?envType=study-plan&id=programming-skills-i>


Here, we first initialize two pointers left and right to 0. We then traverse the array with the right pointer and check if the current element is non-zero. If it is, we swap it with the element at the left pointer and increment left to point to the next non-zero element.

By doing this, we are maintaining the relative order of non-zero elements while moving all zeros to the end of the array. Finally, when the right pointer reaches the end of the array, all non-zero elements would have been swapped to the front of the array and all zeros would have been pushed to the end of the array. Since we are modifying the input array in-place, we do not need to return anything.
