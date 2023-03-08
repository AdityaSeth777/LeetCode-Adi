Question -> https://leetcode.com/problems/koko-eating-bananas/submissions/911338250/



We are given a list of piles of bananas and a time limit h within which Koko wants to finish eating all the bananas. Our task is to determine the minimum integer value of k such that Koko can eat all the bananas within h hours.

To solve this problem, we use binary search. We first define the search range for k as 1 to the maximum number of bananas in any pile, since Koko can't eat more bananas per hour than there are in any one pile. We then use a while loop to perform binary search.

At each iteration, we calculate the number of hours needed to eat all bananas with the current value of k. We do this by looping through all the piles of bananas and adding the time it takes to eat the bananas in each pile with the current k value. The time it takes to eat the bananas in a single pile is calculated by dividing the number of bananas in the pile by k, and then rounding up to the nearest integer using the ceiling division operator //. We keep track of the total time it takes to eat all the bananas in the variable hours.

After calculating the total time needed to eat all the bananas with the current k value, we compare it with the time limit h. If hours is less than or equal to h, it means that Koko can eat all the bananas within the time limit using the current k value. In this case, we update the right pointer to mid - 1 and try a smaller k value to see if it's also possible to eat all the bananas within the time limit. If hours is greater than h, it means that Koko can't eat all the bananas within the time limit using the current k value. In this case, we update the left pointer to mid + 1 and try a larger k value to see if it's possible to eat all the bananas within the time limit.

We repeat this process until the left and right pointers cross each other, at which point the left pointer points to the minimum k value that allows Koko to eat all the bananas within the time limit. We return this left pointer value as the answer.