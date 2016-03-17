Context Relevant technical loop
==
Interview loop 2016-03-17

Prashant
--
Given an array of distinct values, part of which is unsorted,
find the minimal unsorted slice.

Examples:
input: [1, 4, 6, 3, 9]
output: (1, 3) # indices of 4 (insertion point) and 3 (out of order)
input: [6, 1, 2, 3, 9]
output: (0, 3)

Mick
--
Design a tinyurl system.

Using delete, free memory in a binary tree.
Recursive or iterative.

Eugene
--
Find number of recurrences of letters in a string.
Answer: Use a hash (assuming UTF-8 rather than just ASCII)
Follow-up: What about conflicts? Idea: Use a heap in case of
conflicts to guarantee O(lg n) insertion and retrieval time.
