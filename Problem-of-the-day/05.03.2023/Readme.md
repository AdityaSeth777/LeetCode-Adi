Problem -> https://leetcode.com/problems/jump-game-iv/submissions/909310491/


The explanation of the given code:

The minJumps method takes an input list of integers arr and returns an integer value that represents the minimum number of steps required to reach the last index of the array.
First, the length of the input list is calculated and if it's equal to 1, then we are already at the last index and no jumps are required. In this case, we return 0.
Next, a dictionary named indices is created to store the indices of each element in the input list. This will be used to efficiently check for neighbors with the same value in the array during the BFS algorithm.
A queue is initialized as a deque, where the first element is the starting index 0. The visited set is also initialized with 0 as it is the starting index.
The steps variable is also initialized to 0 as the starting index is 0 and no steps have been taken yet.
The BFS algorithm is performed using a while loop that runs until the queue is empty. In each iteration, we pop an element from the left of the queue and store it in the variable curr_index.
If curr_index is equal to the last index of the array, i.e., n-1, then we have reached the last index and we return the number of steps taken.
Otherwise, we check for the neighbors of curr_index by checking curr_index-1 and curr_index+1. If these neighbors are within the array bounds and have not been visited yet, we add them to the queue and mark them as visited in the visited set.
We also check for neighbors with the same value by looking up their indices in the indices dictionary. If a neighbor is found and has not been visited yet, we add it to the queue and mark it as visited in the visited set. We also remove the index list from the indices dictionary to avoid redundant checks.
Finally, we increment steps by 1 at the end of each iteration to keep track of the number of steps taken so far.
If we reach the end of the BFS algorithm without reaching the last index, then we return -1 to indicate that it's not possible to reach the last index from the first index of the array.