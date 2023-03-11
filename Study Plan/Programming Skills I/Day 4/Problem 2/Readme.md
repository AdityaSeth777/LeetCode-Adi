Problem -> https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/submissions/913109493/


The canMakeArithmeticProgression function takes an array arr of integers as input and returns True if the array can be rearranged to form an arithmetic progression. Otherwise, it returns False.

The function first sorts the input array arr. The difference between any two consecutive elements in an arithmetic progression is the same. Therefore, we can determine the common difference by subtracting the first element from the second element of the sorted array.

The function then iterates over the sorted array from index 2 to the end, comparing the difference between the current element and the previous element to the common difference. If any two consecutive elements have a difference that is not equal to the common difference, the array cannot be rearranged to form an arithmetic progression and the function returns False.

If all differences between consecutive elements are equal to the common difference, the array can be rearranged to form an arithmetic progression and the function returns True