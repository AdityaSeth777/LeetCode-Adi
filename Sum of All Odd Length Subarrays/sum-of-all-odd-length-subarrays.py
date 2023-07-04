class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        result = 0
        
        for length in range(1, n+1, 2):
            for i in range(n-length+1):
                j = i + length - 1
                result += sum(arr[i:j+1])
        
        return result