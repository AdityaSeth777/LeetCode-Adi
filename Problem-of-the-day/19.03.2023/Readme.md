Problem -> <https://leetcode.com/problems/design-add-and-search-words-data-structure/description/>


The WordDictionary class has an __init__ method that initializes the root node of the Trie. The addWord method adds a new word to the Trie by traversing the Trie from the root node to the last character of the word, creating new nodes as necessary, and setting the is_word attribute of the last node to True. The search method performs a depth-first search of the Trie to find a matching word or substring. If the current character in the search string is a dot, it recursively searches all child nodes of the current node. If the current character is a letter, it moves to the child node corresponding to that letter. The search is successful if it reaches the end of the search string and the last node is marked as a word.

Note that this implementation assumes that the input words only contain lowercase English letters and dots. If the input words can contain other characters, you may need to modify the code accordingly.
