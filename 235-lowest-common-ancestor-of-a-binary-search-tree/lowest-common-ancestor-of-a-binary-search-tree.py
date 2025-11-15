# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        - if both p and q on the right, go right
        - if both on the left, go left
        - else, return current root
        """
        small = min(p.val, q.val)
        large = max(p.val, q.val)

        d = deque([root])
        while d:
            node = d.popleft()
            if node.val > large:
                d.append(node.left)
            elif node.val < small:
                d.append(node.right)
            else:
                return node