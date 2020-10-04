### Insert into a Binary Search Tree

Given the root node of a binary search tree (BST) and a value to be inserted into the tree, insert the value into the BST. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Note that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

#### Example: 

```
Given the tree:
        4
       / \
      2   7
     / \
    1   3
And the value to insert: 5
You can return this binary search tree:

         4
       /   \
      2     7
     / \   /
    1   3 5

This tree is also valid:

         5
       /   \
      2     7
     / \   
    1   3
         \
          4
```

#### Constraints:

* The number of nodes in the given tree will be between 0 and 10^4.
* Each node will have a unique integer value from 0 to -10^8, inclusive.
-10^8 <= val <= 10^8
* It's guaranteed that val does not exist in the original BST.

#### Note:

* next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
* You may assume that next() call will always be valid, that is, there will be at least a next smallest number in the BST when next() is called.


####  Go to answer

[Insert_into_a_Binary_Search_Tree.py](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Code/Insert_into_a_Binary_Search_Tree.py)

#### Go to review

[Review Page](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/ReviewPage.md)