# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursively        
class Solution:
    def postorderTraversal(self, root):
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
            # dfs find root's left child
            self.helper(root.left, res)
            # dfs find root's right child
            self.helper(root.right, res)
            # put current value in the result
            res.append(root.val)


# Iteratively
class Solution2:
    def postorderTraversal(self, root):
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
                # push left child and right child into stack (first in last out)
                if root.left:
                    stack.append(root.left)
                if root.right:
                    stack.append(root.right)
                
        # reverse result
        return res[::-1]