Problem -> https://leetcode.com/problems/string-compression/submissions/907571078/

The code in details ->

1. We start by defining a function compress that takes an input array of characters chars and returns an integer, which represents the new length of the compressed array.

```bash
class Solution:
    def compress(self, chars: List[str]) -> int:
```

We initialize two pointers, write and start, to 0. These pointers are used to keep track of where to write the compressed characters in the input array and where the current group of consecutive characters starts, respectively.

```bash
        # Initialize pointers
        write = 0
        start = 0
```

We iterate through the input array using a for loop that runs from 0 to len(chars)-1. Inside the loop, we check if the current character is different from the previous one or if we have reached the end of the array.

```bash
        # Iterate through the input array
        for i in range(len(chars)):
            # If the current character is different from the previous one
            if i + 1 == len(chars) or chars[i + 1] != chars[i]:
                ...
```

If the current character is different from the previous one or if we have reached the end of the array, we have finished processing the current group of consecutive characters. We write the first character of the group to the write index of the input array.

```bash
                # Write the current character
                chars[write] = chars[start]
                write += 1
```

If there is more than one occurrence of the current character, we compute the length of the group, convert it to a string, and write each digit of the string to the next write indices of the input array.


```bash
                # If there is more than one occurrence of the current character
                if i > start:
                    # Compute the length of the group and write it
                    for digit in str(i - start + 1):
                        chars[write] = digit
                        write += 1
```

We move the start pointer to the first character of the next group of consecutive characters.

```bash
                # Move the start pointer to the next group
                start = i + 1
```

After the loop, the compressed string is stored in the input array up to the write index. We return write as the new length of the array.

```bash
        # Return the new length of the array
        return write
```

Overall, the algorithm works by iterating through the input array and identifying groups of consecutive characters. For each group, it writes the first character of the group to the output array and, if there is more than one occurrence of the character, writes the length of the group as a string of digits to the output array. The algorithm uses two pointers to keep track of where to write the compressed characters in the input array and where the current group of consecutive characters starts, respectively. The algorithm uses only constant extra space, as required by the problem statement.