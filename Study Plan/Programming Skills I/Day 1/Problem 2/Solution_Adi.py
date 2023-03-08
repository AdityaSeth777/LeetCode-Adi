class Solution:
    def average(self, salary: List[int]) -> float:
        # Exclude the minimum and maximum salary from the list and calculate the sum
        total = sum(salary) - min(salary) - max(salary)
        
        # Calculate the number of employees whose salaries are considered for the average
        count = len(salary) - 2
        
        # Calculate and return the average salary
        return total / count
