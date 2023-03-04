Problem -> https://leetcode.com/submissions/detail/906969992/


Given an array nums, the goal is to find the minimum number of elements that need to be removed in order to transform nums into a mountain array.

A mountain array is defined as an array that can be split into two non-empty parts: the left part is in strictly increasing order, and the right part is in strictly decreasing order. For example, [1, 3, 5, 4, 2] is a mountain array, while [1, 2, 3, 4, 5] and [5, 4, 3, 2, 1] are not.

The algorithm works by first computing the length of the longest increasing subsequence for each index i in nums, and storing the result in the array left. This is done by iterating over all indices j before i, and checking if the element at i is greater than the element at j. If it is, we update left[i] to be the maximum between its current value and left[j] + 1. This ensures that left[i] contains the length of the longest increasing subsequence that ends at i.

The same process is repeated in reverse order to compute the length of the longest decreasing subsequence for each index i in nums, storing the result in the array right.

Finally, the algorithm iterates over all indices i in nums, and computes the sum left[i] + right[i] - 1, which represents the length of the longest mountain subsequence that includes i. The minimum number of elements that need to be removed is then equal to n - res, where n is the length of nums and res is the maximum value of left[i] + right[i] - 1 over all indices i.

The overall time complexity of this algorithm is O(n^2), since we iterate over all pairs of indices i and j. However, it is possible to optimize the algorithm using dynamic programming, resulting in an O(n log n) time complexity.