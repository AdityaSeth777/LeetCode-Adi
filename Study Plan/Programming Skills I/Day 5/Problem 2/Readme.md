Problem -> <https://leetcode.com/problems/next-greater-element-i/description/?envType=study-plan&id=programming-skills-i>


The problem asks us to find the next greater element for each element in a given array nums1 in another array nums2, where each element in nums1 is present in nums2.

The solution defines a function called nextGreaterElement with two input parameters nums1 and nums2. The function returns an array of the next greater elements for each element in nums1.

The function initializes an empty array called result to store the next greater elements. It then iterates over each element num in nums1 using a for...of loop. For each num, it first sets a variable called flag to -1. This flag will be used to indicate if a greater element is found for the current element.

Then, it iterates over nums2 starting from the index of num using a for loop. For each element i in nums2 starting from the index of num, it checks if i is greater than num. If it is, it sets the value of flag to i and breaks out of the loop. This indicates that a greater element than num has been found in nums2.

After iterating over nums2, the function appends the value of flag to the result array. If no greater element than num is found in nums2, flag remains -1 and this value is appended to result.

Finally, the function returns the result array containing the next greater elements for each element in nums1.

In summary, this solution uses nested for loops to find the next greater element for each element in nums1 by iterating over nums2. The result is stored in an array called result and returned by the function.
