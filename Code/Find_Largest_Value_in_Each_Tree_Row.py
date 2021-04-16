# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# BFS Solution
class Solution:
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        # maxes stores results
        maxes = []

        # row is a queue, it stores nodes of tree
        row = [root]
        
        # use any check if queue is empty
        while any(row):
            # get max value
            maxes.append(max(node.val for node in row))

            # push kid of node into queue row
            row = [kid for node in row for kid in (node.left, node.right) if kid]

            # equals to:
            # for node in row:
            #     for kid in (node.left, node.right):
            #         if kid:
            #             row.append(kid)
            
        return maxes

# DFS Solution
class Solution:
    def largestValues(self, root):

        # self.ans stores results
        self.ans = []

        # helper function called
        self.helper(root, 0)
        return self.ans
    
    def helper(self, node, level):
        if not node:
            return

        # get max value of current level
        if len(self.ans) == level:
            self.ans.append(node.val)
        else:
            self.ans[level] = max(self.ans[level], node.val)

        # call helper function for kids of node
        self.helper(node.left, level+1)
        self.helper(node.right, level+1)