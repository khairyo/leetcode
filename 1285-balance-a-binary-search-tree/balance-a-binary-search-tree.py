# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        a = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            a.append(node.val)
            inorder(node.right)
        inorder(root)
        
        def build(l, r):
            if l > r:
                return
            mid = (l+r) // 2
            node = TreeNode(a[mid])
            node.left = build(l, mid-1)
            node.right = build(mid+1, r)
            return node
        
        return build(0, len(a)-1)
