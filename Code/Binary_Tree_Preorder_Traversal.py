# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursively        
class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # set list to store result
        res = []
        # call dfs function
        self.helper(root, res)
        return res
    
    def helper(self, root, res):
        """
        :type root: TreeNode
        :type res: List[int]
        """
        # check if root exists
        if root:
            # put current value in the result
            res.append(root.val)
            # dfs find root's left child
            self.helper(root.left, res)
            # dfs find root's right child
            self.helper(root.right, res)


# Iteratively
class Solution2:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # set list to store result
        res = []
        # set list as stack to store root node and put root in it
        stack = [root]
        
        while stack:
            # get node
            root = stack.pop()

            if root:
                # add value in result
                res.append(root.val)
                # push right child and left child into stack (first in last out)
                if root.right:
                    stack.append(root.right)
                if root.left:
                    stack.append(root.left)
        return res