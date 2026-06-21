# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            tmp1 = root.left
            tmp2 = root.right
            root.left = root.right
            root.right = tmp1
            self.invertTree(tmp1)
            self.invertTree(tmp2)


        return root


        