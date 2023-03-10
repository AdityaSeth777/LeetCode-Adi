class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True) # Sort the array in descending order
        for i in range(len(nums)-2):
            if nums[i] < nums[i+1] + nums[i+2]: # Check if a triangle can be formed
                return nums[i] + nums[i+1] + nums[i+2] # Return the largest perimeter
        return 0 # Return 0 if no triangle can be formed
