from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        # Initialize pointers
        write = 0
        start = 0
        
        # Iterate through the input array
        for i in range(len(chars)):
            # If the current character is different from the previous one
            if i + 1 == len(chars) or chars[i + 1] != chars[i]:
                # Write the current character
                chars[write] = chars[start]
                write += 1
                
                # If there is more than one occurrence of the current character
                if i > start:
                    # Compute the length of the group and write it
                    for digit in str(i - start + 1):
                        chars[write] = digit
                        write += 1
                
                # Move the start pointer to the next group
                start = i + 1
        
        # Return the new length of the array
        return write