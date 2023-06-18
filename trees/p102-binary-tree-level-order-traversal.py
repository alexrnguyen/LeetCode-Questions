# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
            
        def currentLevel(root, nodesInOrder, level):
            if root is None:
                return
            if level >= len(nodesInOrder):
                # Add a new list to represent a level in the tree
                nodesInOrder.append([])
            nodesInOrder[level].append(root.val)
            currentLevel(root.left, nodesInOrder, level + 1)
            currentLevel(root.right, nodesInOrder, level + 1)

        nodesInOrder = []
        currentLevel(root, nodesInOrder, 0)
        return nodesInOrder