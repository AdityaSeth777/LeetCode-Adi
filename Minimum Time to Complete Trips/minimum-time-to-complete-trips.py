from typing import List

class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left, right = 0, max(time) * totalTrips  # initialize left and right pointers
        while left < right:
            mid = (left + right) // 2  # calculate midpoint
            trips = 0
            for t in time:
                trips += mid // t  # calculate number of trips for each bus at time 'mid'
                if trips >= totalTrips:
                    break  # stop the loop if the total number of trips is reached
            if trips >= totalTrips:
                right = mid  # update right pointer if totalTrips is reached
            else:
                left = mid + 1  # update left pointer if totalTrips is not reached
        return left