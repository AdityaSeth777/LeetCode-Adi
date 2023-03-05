from collections import deque
from typing import List

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0
        
        # Create a dictionary to store the indices of each element in the array
        indices = {}
        for i in range(n):
            if arr[i] not in indices:
                indices[arr[i]] = []
            indices[arr[i]].append(i)
        
        # Perform BFS
        queue = deque()
        queue.append(0)
        visited = set()
        visited.add(0)
        steps = 0
        
        while queue:
            size = len(queue)
            for i in range(size):
                curr_index = queue.popleft()
                if curr_index == n - 1:
                    return steps
                
                # Check for neighbors: i-1 and i+1
                for next_index in [curr_index - 1, curr_index + 1]:
                    if next_index >= 0 and next_index < n and next_index not in visited:
                        queue.append(next_index)
                        visited.add(next_index)
                
                # Check for neighbors: j where arr[i] == arr[j]
                if arr[curr_index] in indices:
                    for next_index in indices[arr[curr_index]]:
                        if next_index not in visited:
                            queue.append(next_index)
                            visited.add(next_index)
                    # Remove the index list to avoid redundant checks
                    del indices[arr[curr_index]]
            steps += 1
        
        return -1
