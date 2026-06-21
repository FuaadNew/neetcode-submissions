# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        largest_diameter = [0]
        def dfs(root):
            if not root:
                return 0
            left_height = dfs(root.left)
            right_height = dfs(root.right)
            diameter = left_height + right_height
            largest_diameter[0] = max(largest_diameter[0],diameter)
            return 1 + max(left_height,right_height)
        dfs(root)
        return largest_diameter[0]
        