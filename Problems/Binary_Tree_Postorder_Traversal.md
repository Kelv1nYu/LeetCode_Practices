### Binary Tree Postorder Traversal

**Given the root of a binary tree, return the postorder traversal of its nodes' values.**

#### Example 1:

```
        1
         \
          2
         /
        3

Input: root = [1,null,2,3]
Output: [1,2,3]
```

#### Example 2:

```
Input: root = []
Output: []
```

#### Example 3:

```
Input: root = [1]
Output: [1]
```

#### Example 4:

```
        1
       /
      2
Input: root = [1,2]
Output: [1,2]
```

#### Example 5:

```
        1
         \
          2
Input: root = [1,null,2]
Output: [1,2]
```

#### Constraints:

* The number of the nodes in the tree is in the range [0, 100].
* -100 <= Node.val <= 100

#### Follow up:

Recursive solution is trivial, could you do it iteratively?


####  Go to answer

[Binary_Tree_Postorder_Traversal.py](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Code/Binary_Tree_Postorder_Traversal.py)

#### Go to review

[Review Page](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Review/Python3/Binary_Tree_Postorder_Traversal.md)