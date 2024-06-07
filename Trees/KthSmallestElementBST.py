class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        # nodes visited
        n = 0
        # iterating through the node
        cur = root
        stack = []

        # as long as stack is non empty and curr is non None
        while cur or stack:
            # iterating through the left
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            n += 1

            if n == k:
                return cur.val

            cur = cur.right