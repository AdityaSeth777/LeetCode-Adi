class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()  # sort the array
        result = 0
        for i in range(0, len(nums), 2):
            result += min(nums[i], nums[i+1])  # add the minimum of each pair to the result
        return result