class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        ans = ListNode(0)
        ans.next = head
        curr = ans
        
        while curr.next and curr.next.next:
            t1 = curr.next
            t2 = curr.next.next
            curr.next = t2
            t1.next = t2.next
            t2.next = t1
            curr = curr.next.next
        
        return ans.next