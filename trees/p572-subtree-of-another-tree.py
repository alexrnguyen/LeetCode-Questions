# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """    
        # Checks if all values in both trees are equal
        def checkTree(root, subRoot):
            if root is None or subRoot is None:
                return root is None and subRoot is None
            return root.val == subRoot.val and checkTree(root.left, subRoot.left) and checkTree(root.right, subRoot.right)
        
        if root is None:
            return False
        
        elif checkTree(root, subRoot):
            return True
        
        # Check the left and right subtrees of the root
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)