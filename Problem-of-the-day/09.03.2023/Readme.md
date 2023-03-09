Problem -> https://leetcode.com/problems/linked-list-cycle-ii/submissions/911844450/


Here is how the code works:

First, it checks if the linked list has at least two nodes. If it doesn't, then there can be no cycle, and it returns None.

We initialize two pointers slow and fast to the head of the linked list. The slow pointer moves one step at a time while the fast pointer moves two steps at a time.

We iterate through the linked list using the while loop as long as the fast pointer is not None and fast.next is not None. This ensures that we don't get any null pointer exceptions while traversing the linked list.

In each iteration, we move the slow pointer by one step and the fast pointer by two steps.

If there is a cycle in the linked list, these two pointers will eventually meet at some node in the cycle.

Once they meet, we reset the slow pointer to the head of the linked list and move both slow and fast pointers one step at a time until they meet again. The node where they meet is the starting node of the cycle.

If we reach the end of the linked list without finding a cycle, we return None.