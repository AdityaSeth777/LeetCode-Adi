class Solution:
    def minimizeArrayValue(self, nums):
        total_sum = 0
        result = 0
        for index in range(len(nums)):
            total_sum += nums[index]
            result = max(result, (total_sum + index) // (index + 1))
        return int(result)