Problem -> https://leetcode.com/submissions/detail/911683589/


This code defines a function called average that takes a list of integers called salary and returns the average of all the salaries, excluding the minimum and maximum salaries.

The function first calculates the sum of all the salaries in the list by calling the sum() function on the salary list. It then subtracts the minimum and maximum salaries from this sum by calling the min() and max() functions on the salary list and subtracting their values from the sum. This gives the total salary of all the employees whose salaries are considered for the average.

Next, the function calculates the number of employees whose salaries are considered for the average. This is done by subtracting 2 from the length of the salary list, as the minimum and maximum salaries are excluded from the calculation.

Finally, the function calculates and returns the average salary by dividing the total salary by the number of employees whose salaries are considered for the average.

It is worth noting that if the salary list has less than two elements, the function will return 0.0, as there will not be enough employees to calculate an average. Therefore, it is important to ensure that the salary list has at least two elements before calling the average() function.