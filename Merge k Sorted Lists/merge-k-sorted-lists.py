from heapq import heappush, heappop
from typing import List, Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Create a min-heap to store the heads of all k linked lists
        min_heap = []
        
        # Add the head of each linked list to the min-heap
        for i in range(len(lists)):
            if lists[i]:
                heappush(min_heap, (lists[i].val, i, lists[i]))
        
        # Create a dummy node to serve as the head of the merged linked list
        dummy = ListNode(0)
        curr = dummy
        
        # While there are still nodes in the min-heap
        while min_heap:
            # Pop the node with the smallest value from the min-heap
            val, i, node = heappop(min_heap)
            
            # Add the popped node to the merged linked list
            curr.next = node
            curr = curr.next
            
            # If the popped node has a next node, add it to the min-heap
            if node.next:
                heappush(min_heap, (node.next.val, i, node.next))
                
        return dummy.next