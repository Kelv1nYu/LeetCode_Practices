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
            # dfs find root's left child
            self.helper(root.left, res)
            # put current value in the result
            res.append(root.val)
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
        # set list as stack to store root node
        stack = []
        # assign root to cur
        cur = root
        while cur or stack:
            # loop to find current node's left child and push them into stack
            while cur:
                stack.append(cur)
                cur = cur.left
            
            # get the node
            cur = stack.pop()
            # add value in result
            res.append(cur.val)
            # get the right child of current node
            cur = cur.right
        return res