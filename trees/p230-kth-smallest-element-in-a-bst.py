# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # Iterative Solution
        n = 0 # Number of elements visited
        stack = []
        current = root

        # While current is not None or the stack is not empty
        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            n = n + 1
            if n == k:
                return current.val
            current = current.right