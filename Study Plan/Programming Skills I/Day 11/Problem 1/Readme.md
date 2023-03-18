Problem -> <https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/description/>

This code defines a class Solution with a method sortByBits that takes an integer array arr as input and returns the sorted array.

The method defines a custom comparison function bit_count that takes a number as input and counts the number of ones in its binary representation using bitwise operations.

The method then sorts the array arr using the custom comparison function, first by the number of ones in the binary representation, and then by the number itself in ascending order.

Finally, the sorted array is returned.
