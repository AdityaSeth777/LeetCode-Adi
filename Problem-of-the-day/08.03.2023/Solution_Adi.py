class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # define the search range for k
        left = 1
        right = max(piles)
        
        # perform binary search to find the minimum k
        while left <= right:
            mid = (left + right) // 2
            hours = 0
            for bananas in piles:
                # calculate hours needed to eat bananas in current pile
                hours += (bananas + mid - 1) // mid
            if hours <= h:
                # if it's possible to eat all bananas in h hours with current k
                # then try a smaller k to see if it's also possible
                right = mid - 1
            else:
                # if it's not possible to eat all bananas in h hours with current k
                # then try a larger k to see if it's possible
                left = mid + 1
        
        # the left pointer will point to the minimum k
        return left
