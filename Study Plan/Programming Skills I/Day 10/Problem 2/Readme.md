Problem -> <https://leetcode.com/problems/middle-of-the-linked-list/description/>


In the middleNode method, we first initialize two pointers slow and fast to the head of the linked list. Then, we move the fast pointer two steps at a time and the slow pointer one step at a time using a while loop.

When the fast pointer reaches the end of the linked list, the slow pointer will be at the middle node of the linked list. If there are two middle nodes, we return the second middle node.

Finally, we return the slow pointer as the middle node of the linked list. If the linked list is empty, the method returns None.
