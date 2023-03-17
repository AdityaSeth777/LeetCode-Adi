Problem -> <https://leetcode.com/problems/sum-of-all-odd-length-subarrays/description/?envType=study-plan&id=programming-skills-i>


Here, we first initialize a variable result to 0. Then, we loop through all possible odd lengths starting from 1 up to n (where n is the length of the input array arr) and increment the length by 2 in each iteration.

Within this outer loop, we then loop through all possible subarrays of the current odd length by iterating through the indices i and j such that i ranges from 0 to n-length, and j is set to i+length-1. For each subarray, we compute its sum using the built-in sum function and add it to the result variable.

Finally, we return the accumulated sum result as the answer to the problem.
