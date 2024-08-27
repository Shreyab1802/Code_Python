# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        levels = []

        if not root:
            return levels

        def find_levels(node: TreeNode, level: int):

            if len(levels) == level:
                levels.append([])

            levels[level].append(node.val)

            if node.left:
                find_levels(node.left, level + 1)
            if node.right:
                find_levels(node.right, level + 1)

            return levels

        return find_levels(root, 0)