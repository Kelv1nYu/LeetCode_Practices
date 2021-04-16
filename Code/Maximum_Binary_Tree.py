# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        # Recursive boundary conditions
        if not nums:
            return None
        
        maxNum = max(nums)
        maxIndex = nums.index(maxNum)
        
        root = TreeNode(maxNum)
        
        # Recursively generate left and right subtrees
        root.left = self.constructMaximumBinaryTree(nums[:maxIndex])
        root.right = self.constructMaximumBinaryTree(nums[maxIndex+1:])
            
        return root