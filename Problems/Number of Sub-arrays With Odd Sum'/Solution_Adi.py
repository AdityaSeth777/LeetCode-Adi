class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        odd_count = 0
        even_count = 1
        curr_sum = 0
        for num in arr:
            curr_sum += num
            if curr_sum % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
        return (odd_count * even_count) % (10**9 + 7)
