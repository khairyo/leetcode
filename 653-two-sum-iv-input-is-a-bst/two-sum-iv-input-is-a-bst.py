# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False

        d = deque([root])
        s = set()

        while d:
            node = d.popleft()
            diff = k - node.val
            if diff in s:
                return True
            else:
                s.add(node.val)
                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)
        return False