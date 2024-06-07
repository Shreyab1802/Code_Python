# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        maxStore = []
        self.traverse(root, maxStore)
        # Return the maximum path sum
        return max(maxStore)

    def traverse(self, node, maxStore):

        if not node:
            return 0

        left = self.traverse(node.left, maxStore)
        right = self.traverse(node.right, maxStore)

        if left < 0:
            left = 0
        if right < 0:
            right = 0

        # Update maxStore with the sum of the current path
        maxStore.append(left + right + node.val)

        return max(left, right) + node.val