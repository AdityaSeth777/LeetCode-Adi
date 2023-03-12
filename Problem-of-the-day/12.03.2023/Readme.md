Problem -> <https://leetcode.com/problems/merge-k-sorted-lists/submissions/913682221/>



In this implementation, the min-heap stores tuples containing the value of the node, the index of the linked list it came from, and a reference to the node itself. The heappop function returns the tuple with the smallest value (which is the first element of the tuple), so we can easily add the next node from the linked list that the popped node came from. We continue this process until the min-heap is empty, which means we have merged all the linked lists into one sorted linked list.
