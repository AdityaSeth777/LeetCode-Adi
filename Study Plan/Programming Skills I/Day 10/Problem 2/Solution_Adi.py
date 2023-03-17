class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize two pointers
        slow = head
        fast = head

        # Move the fast pointer two steps at a time and the slow pointer one step at a time
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # At this point, the slow pointer is at the middle node of the linked list
        return slow
