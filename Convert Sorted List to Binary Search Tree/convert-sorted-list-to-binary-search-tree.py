# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # Base case
        if not head:
            return None

        # Find the middle node of the linked list
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Create a new TreeNode with the value of the middle node
        node = TreeNode(slow.val)

        # Split the linked list into two halves
        if prev:
            prev.next = None
            left = head
            right = slow.next
        else:
            left = None
            right = slow.next

        # Recursively build the left and right subtrees
        node.left = self.sortedListToBST(left)
        node.right = self.sortedListToBST(right)

        return node