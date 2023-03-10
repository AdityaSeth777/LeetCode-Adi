Problem -> https://leetcode.com/problems/number-of-1-bits/submissions/912717006/


This is a Python function that calculates the Hamming weight of a given integer, which is the number of '1' bits in its binary representation.

The function hammingWeight takes an integer n as input and returns an integer representing the number of '1' bits in its binary representation.

The function starts by initializing a count variable to zero. It then loops through all the bits in the binary representation of n by shifting n one bit to the right at each iteration, until n becomes zero. This is done using a while loop with the condition n > 0.

At each iteration, the function checks if the rightmost bit of n is equal to 1, by using the bitwise AND operator & with the binary representation of 1. If the result of this operation is 1, it means that the rightmost bit of n is 1, so the function increments the count variable by 1.

After counting all the '1' bits in the binary representation of n, the function returns the count as an integer.

Overall, this function is an efficient way to calculate the Hamming weight of an integer using bitwise operations.