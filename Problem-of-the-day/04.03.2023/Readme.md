Problem -> https://leetcode.com/problems/count-subarrays-with-fixed-bounds/submissions/908942893/



This is an implementation of a solution to the problem of finding the number of fixed-bound subarrays in a given integer array nums with minimum value minK and maximum value maxK.

The solution has two helper functions - findArrays and calculateSubarrays.

The findArrays function takes three parameters - nums, minK, and maxK. It creates an empty list res to store the fixed-bound subarrays and another empty list arr to temporarily store the subarrays. It then iterates through the nums list, checking each value against minK and maxK. If the value is between minK and maxK, it is added to the arr list. If the value is not between minK and maxK, the arr list is checked if it contains both minK and maxK. If it does, the arr list is appended to the res list. Finally, the function returns the res list of fixed-bound subarrays.

The calculateSubarrays function takes three parameters - arr, minK, and maxK. It initializes res to 0 and creates an empty list queue to temporarily store the indices of the subarray. It also initializes prev to 0, which represents the previous index of the last subarray that contains both minK and maxK. The length of the arr list is stored in n. If minK is equal to maxK, the function calculates the number of subarrays containing minK (or maxK) by counting the number of elements in arr and applying the formula (n/2) * (n+1) if n is even, or ((n+1)/2) * n if n is odd. If minK is not equal to maxK, the function iterates through the arr list, checking each element against minK and maxK. If the element is equal to either minK or maxK, the index of the element is added to the queue list. If the element is not equal to either minK or maxK, the function checks if the queue list contains both minK and maxK. If it does, the function removes the first element of the queue list and calculates the number of subarrays containing both minK and maxK using the indices of the removed element, prev, and the current index i. The number of subarrays is added to res, and prev is set to the removed element plus one. The current index i is then added to the queue list. Finally, the function returns res, which represents the number of subarrays containing both minK and maxK in the given arr.

The main body of the solution initializes arrs to the list of fixed-bound subarrays returned by findArrays. It then initializes ans to 0 and iterates through each subarray in arrs. For each subarray, it calls calculateSubarrays and adds the number of subarrays to ans. Finally, the function returns ans, which represents the total number of fixed-bound subarrays in the given nums with minimum value minK and maximum value maxK.



