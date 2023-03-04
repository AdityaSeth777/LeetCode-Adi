Problem -> https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/submissions/908954354/


This solution aims to find the number of subarrays in a given array that have an odd sum.

The solution uses two variables to keep track of the count of even-sum and odd-sum subarrays seen so far. The variable even_count is initialized to 1 because an empty subarray is also considered to have an even sum. Then, it iterates through the array and maintains a running sum curr_sum of the elements seen so far. If the current sum is even, it increments the even_count variable. If the current sum is odd, it increments the odd_count variable.

Finally, the solution calculates the total number of subarrays with an odd sum by multiplying the counts of odd-sum and even-sum subarrays. This is because an odd sum is obtained when an even number of odd elements are added to an even sum, or when an odd number of odd elements are added to an odd sum. The result is returned after taking the modulo 10^9 + 7 to handle large output values.