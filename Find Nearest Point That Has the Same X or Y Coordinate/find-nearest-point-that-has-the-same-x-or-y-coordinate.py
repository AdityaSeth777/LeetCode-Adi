class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_dist = float('inf') # Initialize minimum distance to infinity
        min_index = -1 # Initialize minimum index to -1
        for i in range(len(points)):
            if points[i][0] == x or points[i][1] == y: # Check if point is valid
                dist = abs(points[i][0] - x) + abs(points[i][1] - y) # Calculate Manhattan distance
                if dist < min_dist: # Update minimum distance and index if distance is smaller
                    min_dist = dist
                    min_index = i
        return min_index # Return index of the valid point with smallest Manhattan distance