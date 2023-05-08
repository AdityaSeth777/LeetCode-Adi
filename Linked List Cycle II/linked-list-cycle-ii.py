class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        
        slow = head
        fast = head
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
            # If there is a cycle
            if slow == fast:
                # Move slow pointer back to head
                slow = head
                
                # Find the point where cycle starts
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                    
                return slow
        
        # No cycle found
        return None