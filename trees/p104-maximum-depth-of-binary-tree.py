# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Depth First Search
        def dfs(root, maximum):
            if root is None:
                return maximum
            return max(dfs(root.left, maximum+1), dfs(root.right, maximum+1))

        if root is None:
            return 0
        maximum = 1
        maximum = max(dfs(root.left, maximum), dfs(root.right, maximum))
        return maximum