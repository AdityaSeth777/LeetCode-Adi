class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        # Initialize a variable to keep track of the decimal value
        decimal_value = 0

        # Traverse the linked list from the head to the tail
        current_node = head
        while current_node:
            # Update the decimal value by shifting it to the left and adding the current node's value
            decimal_value = (decimal_value << 1) | current_node.val

            # Move on to the next node
            current_node = current_node.next

        # Return the final decimal value
        return decimal_value
